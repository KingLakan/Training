from ast import Pass
from operator import sub
import clr
import pathlib
import subprocess
import argparse
import sys
import System
import time
from System.Collections import *

sys.path.append("c:\\Program Files (x86)\\National Instruments \
                \\VeriStand 2020\\nivs.lib\\Reference Assemblies")
clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
clr.AddReference("NationalInstruments.VeriStand")

#USING niveristand Python API to run sequence
from engine_demo_basic import run_engine_demo
from niveristand import run_py_as_rtseq
from niveristand.errors import RunError
from niveristand.legacy import NIVeriStand

from NationalInstruments.VeriStand.ClientAPI import Factory, SystemState
from NationalInstruments.VeriStand import Error

def StartGateway():
    """Start Veristand silent gateway

    Returns:
        bool: true if Server running
    """
    Veristand_gateway_path = (r"c:\Program Files (x86)\National Instruments" 
                              r"\VeriStand 2020\veristand-server.exe")
    output = subprocess.check_output([Veristand_gateway_path,'start'])
    status_output = (output.decode(('UTF-8')).split()[0] + " " +
                     output.decode(('UTF-8')).split()[1])
    print(status_output)
    if status_output == "Server running":
        return True
    else:
        pass#exit(1)

def StopGateway():
    """Stop Veristand silent gateway

    Returns:
        bool: true if Server is stopped
    """
    Veristand_gateway_path = (r"c:\Program Files (x86)\National Instruments" 
                              r"\VeriStand 2020\veristand-server.exe")
    output = subprocess.check_output([Veristand_gateway_path,'stop'])
    status_output = (output.decode(('UTF-8')).split()[0] + " " +
                     output.decode(('UTF-8')).split()[1])
    print(status_output)
    if status_output == "Server stopped":
        return True
    else:
        pass#exit(1)

class DeploymentHandler:


    def __init__(self, system_definition_path: str):
        self.error_check_ = Error()
        self.factory_ = Factory()
        self.factory_workspace_interface_ = (Factory().
                                             GetIWorkspace2('localhost'))
        self.system_definition_path = system_definition_path


    def Deploy(self):
        deploy_system_definition = System.Boolean(True)
        timeout = System.UInt32(500000)
        self.error_check_ = (self.factory_workspace_interface_.
                             ConnectToSystem(self.system_definition_path,
                                             deploy_system_definition,
                                             timeout))
        print("Deploy isError", self.error_check_.IsError)


    def UnDeploy(self):
        password = System.String("")
        undeploy = System.Boolean(True)
        self.error_check_ = (self.factory_workspace_interface_.
                             DisconnectFromSystem("",undeploy))
        print("Undeploy error: ", self.error_check_.IsError)


    def PrintSystemStatus(self):
        """Gets the current state of the system to which the 
           VeriStand Gateway is connected.
        """
        system_definition_file = System.String("")
        targets = System.Array[System.String]([])
        system_definition_file_retured = System.String("")
        targets_returned = System.Array[System.String]([])
        enum_system_state = SystemState.Active

        #print(type(SystemState))
        (self.error_check_,
         enum_system_state,
         system_definition_file_retured,
         targets_returned) = (self.factory_workspace_interface_.
                              GetSystemState(enum_system_state,
                                             system_definition_file,
                                             targets))

        print("SystemState Status, IsError: ", self.error_check_.IsError)
        print("SystemState Status, SystemState status: ", enum_system_state)
        print("Status getSystemState,SystemDefinitionFile Loaded : ",
               system_definition_file_retured)
        for i in targets_returned:
            print("Status getSystemState,Current-Target: ", i)


if __name__ == "__main__":
    #make sure package is installed
    #response = subprocess.check_call(['py.exe','-m','pip','install', 'niveristand'])
    # if not subprocess.check_call(['py.exe','-m','pip','install', 'niveristand']):
    #     print("already installed")
    #StartGateway()
    #StopGateway()
    test = DeploymentHandler("C:\\Users\\dsamuels\\Documents\\VeriStand Projects\\Engine Demo 2\\Engine Demo.nivssdf")
    test.PrintSystemStatus()
    test.Deploy()
    test.PrintSystemStatus()


    # Uses Python real-time sequences to run a test.
    run_py_as_rtseq(run_engine_demo)
    print("Test Success")
    # time.sleep(15)
    # StopGateway()
    # test.UnDeploy()
    # test.PrintSystemStatus()

    # parser = argparse.ArgumentParser(description='SysDef to be processed')
    # parser.add_argument('--file',
    #                     metavar='FILE_PATH',
    #                     type=str,
    #                     action='store',
    #                     help='Path+name of file to append to')
    # args = parser.parse_args()

    # print("inputted file: {}".format(args.file), "\n")

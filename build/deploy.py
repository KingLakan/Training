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

from NationalInstruments.VeriStand.SystemDefinitionAPI import SystemDefinition, Database, CANPort, XNETDatabases, SignalBasedFrame
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
        exit(1)

class DeploymentHandler():
    __init__():
        self.errorCheck = Error()

def Init():
    errorCheck = Error()

    #Factory provides access to the NI VeriStand system and the various interfaces available in the Execution API
    factory = Factory()

    #Interface to perform basic workspace operations, such as getting, setting, and logging channel data.
    factoryWorkspaceInterface = factory.GetIWorkspace2('localhost')

    #SystemDefinition
    SystemDefinitionFilePath = System.String("C:\\Users\\dsamuels\\Documents\\VeriStand Projects\\Engine Demo 2\\Engine Demo.nivssdf")
    #SystemDefinitionFilePath = r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 20\Engine Demo.nivssdf"
    print(SystemDefinitionFilePath)

    deploySystemDefinition = System.Boolean(True)
    timeout = System.UInt32(500000)
    #Connects the VeriStand Gateway to one or more targets and deploys the system definition file.
    errorCheck = factoryWorkspaceInterface.ConnectToSystem(SystemDefinitionFilePath, deploySystemDefinition, timeout)
    print(errorCheck.Code)

    #Gets the current state of the system to which the VeriStand Gateway is connected.
    #signalArray = System.Array[System.String](["Sig1","Sig2","Sig3"])
    systemDefinitionFile = System.String("")
    targets = System.Array[System.String]([])
    systemDefinitionFile_retured = System.String("")
    targets_returned = System.Array[System.String]([])
    enumSystemState = SystemState.Active
    enumSystemState1 = SystemState.Idle

    #print(type(SystemState))
    errorCheck,enumSystemState,systemDefinitionFile_retured,targets_returned = factoryWorkspaceInterface.GetSystemState(enumSystemState, systemDefinitionFile, targets)
    print("Status getSystemState,error: ", errorCheck)
    print("Status getSystemState,SystemState status: ", enumSystemState)
    print("Status getSystemState,SystemDefinitionFile Loaded : ", systemDefinitionFile_retured)
    for i in targets_returned:
        print("Status getSystemState,Current-Target: ", i)

if __name__ == "__main__":
    StartGateway()
    #Init()
    # parser = argparse.ArgumentParser(description='SysDef to be processed')
    # parser.add_argument('--file',
    #                     metavar='FILE_PATH',
    #                     type=str,
    #                     action='store',
    #                     help='Path+name of file to append to')
    # args = parser.parse_args()

    # print("inputted file: {}".format(args.file), "\n")

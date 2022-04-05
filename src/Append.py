import argparse

import clr
import sys
import os
import System
import errno
from System.Collections import *
from os.path import exists


sys.path.append("c:\\Program Files (x86)\\National Instruments\\VeriStand 2020\\nivs.lib\\Reference Assemblies")
clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
clr.AddReference("NationalInstruments.VeriStand")

from NationalInstruments.VeriStand.SystemDefinitionAPI import SystemDefinition, Model, NodeIDUtil, Models
from NationalInstruments.VeriStand import Error 

class Models:
    
    def __init__(self,system_definition_path: str):
        """Create model object from path

        Args:
            system_definition_path (str): path to system def file path = path + filename.nivssdf
        """
        try:
            if exists(system_definition_path):
                self.__systemDefinitionObject = SystemDefinition(system_definition_path)
                self.__DefineObjects()
                print("it exists")
            else:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), system_definition_path)
        except FileNotFoundError as e:
            print(e)

    def __DefineObjects(self):
        self.__firstTarget = self.__systemDefinitionObject.Root.GetTargets().GetTargetList()[0]
        self.__modelsSection = self.__firstTarget.GetSimulationModels().GetModels()
        self.__modelsObject = self.__firstTarget.GetSimulationModels().GetModels().GetModels()
        [print("Models: ", i.Name) for i in self.__modelsObject]
        print("modelsSection:", self.__modelsSection.Name)

    def AddModel(self): # add str as input to choose model to add
        # C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 4\Model\Engine Demo.dll
        __modelName = System.String("Engine Demo 2")
        __modelDesc = System.String("")
        __modelPath = System.String(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 4\Model\Engine Demo.dll")
        __processor = System.Int32(0)
        __decimation = System.Int32(1)
        __initialState = System.UInt16(0)
        __segmentsVectors = System.Boolean(False)
        __importParameters = System.Boolean(True)
        __importSignals = System.Boolean(True)
        # Create a model object
        __myNewModel = Model( __modelName,
                            __modelDesc,
                            __modelPath,
                            __processor,
                            __decimation,
                            __initialState,
                            __segmentsVectors,
                            __importParameters,
                            __importSignals )

        # Add models to project
        self.__modelsSection.AddModel(__myNewModel)

    def AddAliases(self):
        # Hardcoded for engine demo
        # Read current set outports, return channel objects
        __modelOutput1 = self.__modelsSection.GetModels()[0].GetOutportsSection().GetOutports()[0]
        __modelOutput2 = self.__modelsSection.GetModels()[0].GetOutportsSection().GetOutports()[1]
        __modelDesc = System.String("")
        __error = Error()
        # i = 0 # SKAPA EN GENERISK FUNKTION FÖR ATT TESTA
        # while(1):# Check nr of indexes
        #     try:
        #         __modelOutput1 = self.__modelsSection.GetModels()[0].GetOutportsSection().GetOutports()[i]
        #     except IndexError as e:
        #         if e:
        #             print("Error",e)
        #             break
        #     i += 1
        #     print(i,"\n")
        print("__modelOutput: ", __modelOutput1.Name)
        print("__modelOutput: ", __modelOutput2.Name)

        # Set Aliases
        __name1 = System.String("Outport0 Engine model ALIAS")
        __name2 = System.String("Outport1 Engine model ALIAS")
        self.__systemDefinitionObject.Root.GetAliases().AddNewAliasByReference(__name1,__modelDesc,__modelOutput1,__error)
        self.__systemDefinitionObject.Root.GetAliases().AddNewAliasByReference(__name2,__modelDesc,__modelOutput2,__error)

    def SaveSystemDefinition(self):
        __error = System.String("")
        __error_out = System.String("")
        __functionReturn, __error_out = self.__systemDefinitionObject.SaveSystemDefinitionFile(__error)

        if (not __error_out):
            print("File saved")
        else:
            print(__error_out)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='SysDef to be processed')
    parser.add_argument('--file',
                        metavar='FILE_PATH',
                        type=str,
                        action='store',
                        help='Path+name of file to append to')
    args = parser.parse_args()

    print("inputted file: {}".format(args.file), "\n")

    apa = Models(args.file) #repr -> to raw string
    apa.AddModel()
    apa.AddAliases()
    apa.SaveSystemDefinition()


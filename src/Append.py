
import os
import argparse
import clr
import sys
import errno
from os.path import exists
import System # noqa
from System.Collections import * # noqa


sys.path.append("c:\\Program Files (x86)\\National Instruments\\VeriStand 2020\\nivs.lib\\Reference Assemblies")
clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
clr.AddReference("NationalInstruments.VeriStand")

from NationalInstruments.VeriStand.SystemDefinitionAPI import SystemDefinition, Model, NodeIDUtil, Models # noqa
from NationalInstruments.VeriStand import Error # noqa

class Models:
    """Append models to a System Definition file."""

    def __init__(self,system_definition_path: str):
        """Create model object from path

        Args:
            system_definition_path (str): path to system def file path = path + filename.nivssdf
        """

        try:
            if exists(system_definition_path):
                self._system_definition_object = SystemDefinition(system_definition_path)
                self._DefineVeristandObjects()
                print("it exists")
            else:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), system_definition_path)
        except FileNotFoundError as e:
            print(e)

    def _DefineVeristandObjects(self):
        """Define Veristand attributes"""

        self._firstTarget = self._system_definition_object.Root.GetTargets().GetTargetList()[0]
        self._models_selection = self._firstTarget.GetSimulationModels().GetModels()
        self._models_object = self._firstTarget.GetSimulationModels().GetModels().GetModels()
        [print("Models: ", i.Name) for i in self._models_object]
        print("modelsSection:", self._models_selection.Name)

    def AddModel(self): # add str as input to choose model to add
        """Add/Append model to System definition file."""
        # C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 4\Model\Engine Demo.dll
        _model_name = System.String("Engine Demo 2")
        _model_desc = System.String("")
        _model_path = System.String(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 4\Model\Engine Demo.dll")
        _processor = System.Int32(0)
        _decimation = System.Int32(1)
        _initial_state = System.UInt16(0)
        _segments_vectors = System.Boolean(False)
        _import_parameters = System.Boolean(True)
        _import_signals = System.Boolean(True)
        # Create a model object
        _my_new_model = Model( _model_name,
                            _model_desc,
                            _model_path,
                            _processor,
                            _decimation,
                            _initial_state,
                            _segments_vectors,
                            _import_parameters,
                            _import_signals )

        # Add models to project
        self._models_selection.AddModel(_my_new_model)

    def AddAliases(self):
        """Add Aliases for the model to the system definition file."""
        # Hardcoded for engine demo
        # Read current set outports, return channel objects
        _model_output_1 = self._models_selection.GetModels()[0].GetOutportsSection().GetOutports()[0]
        _model_output_2 = self._models_selection.GetModels()[0].GetOutportsSection().GetOutports()[1]
        _model_desc = System.String("")
        _error = Error()
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
        print("_modelOutput: ", _model_output_1.Name)
        print("_modelOutput: ", _model_output_2.Name)

        # Set Aliases
        _name1 = System.String("Outport0 Engine model ALIAS")
        _name2 = System.String("Outport1 Engine model ALIAS")
        self._system_definition_object.Root.GetAliases().AddNewAliasByReference(_name1,_model_desc,_model_output_1,_error)
        self._system_definition_object.Root.GetAliases().AddNewAliasByReference(_name2,_model_desc,_model_output_2,_error)

    def SaveSystemDefinition(self):
        """Save changes to the system definition file."""
        _error = System.String("")
        _error_out = System.String("")
        _function_return, _error_out = self._system_definition_object.SaveSystemDefinitionFile(_error)

        if (not _error_out):
            print("File saved")
        else:
            print(_error_out)

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


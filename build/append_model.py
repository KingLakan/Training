
import os
import argparse
import clr
import sys
import errno
from os.path import exists
import System # noqa
from System.Collections import * # noqa


sys.path.append("c:\\Program Files (x86)\\National Instruments \
                \\VeriStand 2020\\nivs.lib\\Reference Assemblies")
clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
clr.AddReference("NationalInstruments.VeriStand")

from NationalInstruments.VeriStand.SystemDefinitionAPI import \
     SystemDefinition, Model, NodeIDUtil # noqa
from NationalInstruments.VeriStand import Error # noqa


class Models:
    """Append models to a System Definition file."""

    def __init__(self, system_definition_path: str):
        """Class method from_system_definition_path triggers initialization 
           of the __init__ method.

        Args:
            system_definition_path (str): path to system def file
            path = path + filename.nivssdf
        """
        self._system_definition_object = \
            SystemDefinition(system_definition_path)
        self._firstTarget = (self._system_definition_object.Root.GetTargets().
                             GetTargetList()[0])
        self._models_selection = (self._firstTarget.GetSimulationModels().
                                  GetModels())
        self._models_object = (self._firstTarget.GetSimulationModels().
                               GetModels().GetModels())

    @classmethod
    def from_system_definition_path(cls, system_definition_path: str):
        """Used as constructor for the Models class

        Args:
            system_definition_path (str): path + filename of systemdefinition 
            file

        Returns:
            _type_: Object of class
        """
        try:
            cls._ValidatePath(system_definition_path)
        except FileNotFoundError as e:
            print(e)
        return cls(system_definition_path)

    @staticmethod
    def _ValidatePath(system_definition_path: str):
        if not (exists(system_definition_path) and
                system_definition_path.endswith('.nivssdf')):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                    system_definition_path)

    def AddModel(self, model_path):  # add str as input to choose model to add
        """Add/Append model to System definition file."""
        # C:\Users\dsamuels\Documents\VeriStand Projects\
        # Engine Demo 4\Model\Engine Demo.dll
        _model_error = Error()
        self._model_added = None
        _model_name = System.String("Engine Demo 2")
        _model_desc = System.String("")
        self._model_path = model_path
        _processor = System.Int32(0)
        _decimation = System.Int32(1)
        _initial_state = System.UInt16(0)
        _segments_vectors = System.Boolean(False)
        _import_parameters = System.Boolean(True)
        _import_signals = System.Boolean(True)
        # Create a model object
        _my_new_model = Model(_model_name,
                              _model_desc,
                              self._model_path,
                              _processor,
                              _decimation,
                              _initial_state,
                              _segments_vectors,
                              _import_parameters,
                              _import_signals)

        # Add models to project
        [self._model_added,_model_error] = (self._models_selection.
                                         AddModel(_my_new_model, _model_error))
        return self._model_added

    def AddAliases(self):
        """Add Aliases from the model to the system definition file."""
        _model_desc = System.String("")
        _error = Error()
        # Read
        _array_of_model_outPorts = (self._models_selection.GetModels()[0].
                                    GetOutportsSection().GetOutports())
        _array_of_model_inPorts = (self._models_selection.GetModels()[0].
                                   GetInportsSection().GetInports())
        _array_of_model_parameters = (self._models_selection.GetModels()[0].
                                      GetParametersSection().GetParameters())
        _array_of_model_signals = (self._models_selection.GetModels()[0].
                                   GetParametersSection().GetParameters())

        # Write Aliases
        for n in range(0, len(_array_of_model_outPorts)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(_array_of_model_outPorts[n].Name,
                                    _model_desc,
                                    _array_of_model_outPorts[n],
                                    _error))
        for n in range(0, len(_array_of_model_inPorts)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(_array_of_model_inPorts[n].Name,
                                    _model_desc,
                                    _array_of_model_inPorts[n],
                                    _error))
        for n in range(0, len(_array_of_model_parameters)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(_array_of_model_parameters[n].Name,
                                    _model_desc,
                                    _array_of_model_parameters[n],
                                    _error))
        for n in range(0, len(_array_of_model_signals)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(_array_of_model_signals[n].Name,
                                    _model_desc,
                                    _array_of_model_signals[n],
                                    _error))

        # [print("OutPorts: ", i.Name) for i in _array_of_model_outPorts]
        # [print("InPorts: ", i.Name) for i in _array_of_model_inPorts]
        # [print("Parameters: ", i.Name) for i in _array_of_model_parameters]
        # [print("Parameters: ", i.Name) for i in _array_of_model_signals]
        print("Aiases written ok")

    def SaveSystemDefinition(self):
        """Save changes to the system definition file."""
        _error = System.String("")
        _error_out = System.String("")
        _function_return, _error_out = self._system_definition_object. \
            SaveSystemDefinitionFile(_error)

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

    # apa = Models(args.file)  # repr -> to raw string
    apa = Models.from_system_definition_path(args.file)
    apa.AddModel(System.String(r"C:\Users\dsamuels\Documents"
                                    r"\VeriStand Projects\Engine Demo 4"
                                    r"\Model\Engine Demo.dll"))
    apa.SaveSystemDefinition()
    # apa.AddAliases()
    apa.AddAliases()
    apa.SaveSystemDefinition()


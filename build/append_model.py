
import os
import argparse
import clr
import sys
import errno
import pathlib
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
        """Add/Append model to System definition file

        Args:
            model_path (str): Path to model binary file

        Returns:
            bool: Model loaded
        """
        model_error = Error()
        model_added = None
        model_name = System.String("Loaded model")
        model_desc = System.String("")
        model_path = model_path
        processor = System.Int32(0)
        decimation = System.Int32(1)
        initial_state = System.UInt16(0)
        segments_vectors = System.Boolean(False)
        import_parameters = System.Boolean(True)
        import_signals = System.Boolean(True)
        # Create a model object
        my_new_model = Model(model_name,
                             model_desc,
                             model_path,
                             processor,
                             decimation,
                             initial_state,
                             segments_vectors,
                             import_parameters,
                             import_signals)

        # Add models to project
        [model_added, model_error] = (self._models_selection.
                                      AddModel(my_new_model, model_error))
        return model_added

    def AddAliases(self):
        """Add Aliases from the model to the system definition file."""
        model_desc = System.String("")
        error = Error()
        # Read
        array_of_model_outPorts = (self._models_selection.GetModels()[0].
                                   GetOutportsSection().GetOutports())
        array_of_model_inPorts = (self._models_selection.GetModels()[0].
                                  GetInportsSection().GetInports())
        array_of_model_parameters = (self._models_selection.GetModels()[0].
                                     GetParametersSection().GetParameters())
        array_of_model_signals = (self._models_selection.GetModels()[0].
                                  GetParametersSection().GetParameters())

        # Write Aliases
        for n in range(0, len(array_of_model_outPorts)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(array_of_model_outPorts[n].Name,
                                    model_desc,
                                    array_of_model_outPorts[n],
                                    error))
        for n in range(0, len(array_of_model_inPorts)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(array_of_model_inPorts[n].Name,
                                    model_desc,
                                    array_of_model_inPorts[n],
                                    error))
        for n in range(0, len(array_of_model_parameters)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(array_of_model_parameters[n].Name,
                                    model_desc,
                                    array_of_model_parameters[n],
                                    error))
        for n in range(0, len(array_of_model_signals)):
            (self._system_definition_object.Root.GetAliases().
             AddNewAliasByReference(array_of_model_signals[n].Name,
                                    model_desc,
                                    array_of_model_signals[n],
                                    error))

        # [print("OutPorts: ", i.Name) for i in _array_of_model_outPorts]
        # [print("InPorts: ", i.Name) for i in _array_of_model_inPorts]
        # [print("Parameters: ", i.Name) for i in _array_of_model_parameters]
        # [print("Parameters: ", i.Name) for i in _array_of_model_signals]
        print("Aiases written ok")

    def SaveSystemDefinition(self):
        """Save changes to the system definition file."""
        error = System.String("")
        error_out = System.String("")
        file_saved, error_out = self._system_definition_object. \
            SaveSystemDefinitionFile(error)

        if (not error_out):
            print("File saved")
            return file_saved
        else:
            print(error_out)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='SysDef to be processed')
    parser.add_argument('--file',
                        metavar='FILE_PATH',
                        type=str,
                        action='store',
                        help='Path+name of file to append to')
    args = parser.parse_args()

    print("inputted file: {}".format(args.file), "\n")

    veristand = Models.from_system_definition_path(args.file)
    model_path = pathlib.Path(pathlib.Path.cwd().parent,
                              'bin', 'Engine Demo.dll')
    veristand.AddModel(System.String(str(model_path)))
    print("Model written ok")
    veristand.SaveSystemDefinition()
    # apa.AddAliases()
    veristand.AddAliases()
    veristand.SaveSystemDefinition()


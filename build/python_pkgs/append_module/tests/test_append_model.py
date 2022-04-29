from unittest.mock import patch
import pytest
from append_module.append_model import Models
import clr
import System # noqa

#valid_model_path = System.String(r"C:\Users\dsamuels\Documents"
#                                    r"\VeriStand Projects\Engine Demo 4"
#                                    r"\Model\Engine Demo.dll")
#invalid_model_path = System.String(r"")

#existing_path = (r"C:\Users\dsamuels\Documents\VeriStand Projects"
#                     r"\Engine Demo 2\Engine Demo.nivssdf")

@pytest.fixture
def Valid_model_path():
    valid_model_path = System.String(r"C:\Users\dsamuels\Documents"
                                     r"\VeriStand Projects\Engine Demo 4"
                                     r"\Model\Engine Demo.dll")
    return valid_model_path

@pytest.fixture
def Invalid_model_path():
    invalid_model_path = System.String(r"")
    return invalid_model_path

@pytest.fixture
def Invalid_sys_def_path():
    invalid_sys_def_path = ""
    return invalid_sys_def_path

@pytest.fixture
def Existing_path():
    existing_path = (r"C:\Users\dsamuels\Documents\VeriStand Projects"
                     r"\Engine Demo 2\Engine Demo.nivssdf")
    return existing_path

def test_if_valid_path(Invalid_sys_def_path):
    with pytest.raises(FileNotFoundError):
        Models._ValidatePath(Invalid_sys_def_path)


def test_model_added_true(Valid_model_path,Existing_path):
    obj = Models.from_system_definition_path(Existing_path)
    assert obj.AddModel(Valid_model_path) == True


def test_Add_model_paths(Existing_path, Invalid_model_path, Valid_model_path):
    obj = Models.from_system_definition_path(Existing_path)
    with pytest.raises(System.ArgumentException):
        obj.AddModel(Invalid_model_path)
        assert obj._model_added == False
    assert obj.AddModel(Valid_model_path) == True
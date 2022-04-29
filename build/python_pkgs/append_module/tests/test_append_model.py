from unittest.mock import patch
import pytest
from append_module.append_model import Models
import clr
import System # noqa

valid_model_path = System.String(r"C:\Users\dsamuels\Documents"
                                    r"\VeriStand Projects\Engine Demo 4"
                                    r"\Model\Engine Demo.dll")
invalid_model_path = System.String(r"")

existing_path = (r"C:\Users\dsamuels\Documents\VeriStand Projects"
                     r"\Engine Demo 2\Engine Demo.nivssdf")

def test_if_valid_path(mocker):
    with pytest.raises(FileNotFoundError):
        Models._ValidatePath("")


def test_model_added_true(mocker):
    obj = Models.from_system_definition_path(existing_path)
    assert obj.AddModel(valid_model_path) == True

def test_model_paths(mocker):
    obj = Models.from_system_definition_path(existing_path)
    with pytest.raises(System.ArgumentException):
        obj.AddModel(invalid_model_path)
        assert obj._model_added == False
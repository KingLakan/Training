import sys
import pathlib
import pytest
import clr # noqa
import System # noqa

sys.path.append(str(pathlib.Path(pathlib.Path.cwd().parent.parent.parent,
                                 'build')))
from append_model import Models # noqa


@pytest.fixture
def Valid_model_path():
    valid_model_path = pathlib.Path(pathlib.Path.cwd().parent.parent.parent,
                                    'bin', 'Engine Demo.dll')
    return str(valid_model_path)


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
    existing_path = pathlib.Path(pathlib.Path.cwd().parent.parent.parent,
                                 'veristand', 'Engine Demo.nivssdf')
    # existing_path = (r"C:\Users\dsamuels\Documents\VeriStand Projects"
    #                  r"\Engine Demo 2\Engine Demo.nivssdf")
    return str(existing_path)


def test_if_valid_path(Invalid_sys_def_path):
    with pytest.raises(FileNotFoundError):
        Models._ValidatePath(Invalid_sys_def_path)


def test_model_added_true(Valid_model_path, Existing_path):
    obj = Models.from_system_definition_path(Existing_path)
    assert obj.AddModel(Valid_model_path) == True


def test_Add_model_paths(Existing_path, Invalid_model_path, Valid_model_path):
    obj = Models.from_system_definition_path(Existing_path)
    with pytest.raises(System.ArgumentException):
        obj.AddModel(Invalid_model_path)
        assert obj.AddModel() == False
    assert obj.AddModel(Valid_model_path) == True
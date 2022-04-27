import pytest
from unittest.mock import patch

from os.path import exists
from append_module import append_model

def test_check_if_Valid(mocker):
    obj = append_model.Models(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf")
    with pytest.raises(FileNotFoundError):
        obj._CheckIfValidFile("")

def test_define_veristand_objects(mocker):
    mocker.patch.object(append_model.Models,'_DefineVeristandObjects') # mock class 
    obj = append_model.Models(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf")
    obj._DefineVeristandObjects.assert_called()

# @patch.object(append_model.Models,'_DefineVeristandObjects')
# def test_define_veristand_objects(mock_method):
#     append_model.Models(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf")
#     mock_method.assert_called()
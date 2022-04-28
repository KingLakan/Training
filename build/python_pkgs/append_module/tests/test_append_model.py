import pytest
from append_module.append_model import Models


def test_check_if_Valid(mocker):
    with pytest.raises(FileNotFoundError):
        Models._ValidatePath("")

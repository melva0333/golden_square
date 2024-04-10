import pytest
from lib.present import *

def test_present_is_None():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present_is_not_None():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap("toy")
        present.wrap("toy")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
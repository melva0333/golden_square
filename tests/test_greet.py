from lib.greet import *

def test_greet():
    result = greet("Selva")
    assert result == "Hello, Selva!"

from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword():
    result = check_codeword("hole")
    assert result == "Close, but nope."    

def test_check_codeword():
    result = check_codeword("selva")
    assert result == "WRONG!"
from lib.report_length import *

def test_report_length_returns_string_with_length():
    result = report_length("Hello, my name is Selva.")
    assert result == "This string was 24 characters long."
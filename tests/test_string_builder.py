from lib.string_builder import *

def test_help_user_build_a_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("Selva")
    result = stringbuilder.size()
    assert result == 5 
    result = stringbuilder.output()
    assert result == "Selva"

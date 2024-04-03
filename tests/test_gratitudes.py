from lib.gratitudes import *

def test_return_a_gratitude_string():
    gratitudes = Gratitudes()
    gratitudes.add("Peace")
    result = gratitudes.format()
    assert result == "Be grateful for: Peace"
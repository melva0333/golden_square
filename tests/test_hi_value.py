from lib.hi_value import *

def test_first_value_is_higher():
    hi_value = HighValue(5,1)
    result = "First value is higher"
    actual = hi_value.get_highest()
    assert result == actual

def test_second_value_is_higher():
    hi_value = HighValue(-1,5)
    result = "Second value is higher"
    actual = hi_value.get_highest()
    assert result == actual

def test_values_are_equal():
    hi_value = HighValue(5,5)
    result = "Values are equal"
    actual = hi_value.get_highest()
    assert result == actual

def test_first_value_increase_by_two():
    hi_value = HighValue(7,5)
    hi_value.add(2,"first")
    result = 9
    actual = hi_value.value_first
    assert result == actual


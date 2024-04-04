# This is the naive approach
# File: tests/test_reminder.py

# from lib.reminder_error import *


# def test_reminder():
#     reminder_error = Reminder_error("Kay")
#     result = reminder_error.remind()
#     assert result == "No reminder set!"


# this is the new approach

# File: tests/test_reminder.py

import pytest # <-- New code
from lib.reminder_error import *


def test_reminder():
    reminder_error = Reminder_error("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder_error.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"

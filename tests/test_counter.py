from lib.counter import *

def test_help_the_user_to_keep_count():
    counter = Counter()
    counter.add(1)
    result = counter.report()
    assert result == "Counted to 1 so far."


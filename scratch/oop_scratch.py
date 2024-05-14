class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
clicker.click()
assert clicker.read() == 3, "after three clicks, clicker should have count 3"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

def and_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ' and '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"
assert twice(and_repeater, "type hints") == "type hints and type hints"
print(twice(and_repeater, "type hints"))
      
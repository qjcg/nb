#!/usr/bin/env python3
"""A little script that we can debug.

This script will iterate through interger values and blah blah blah...
"""


class Instructor:
    """An instructor represents a training instructor.

    Examples:
        >>> i = Instructor()
        >>> i.name
        'John Gosset'

        >>> i.id
        42

        >>> i2 = Instructor("Jerry Q. Hacker")
        >>> i2.name
        'Jerry Q. Hacker'
    """
    def __init__(self, name='John Gosset', id=42):
        self.name = name
        self.id = id


def do_iteration():
    """The do_iteration function iterates through 10 ints.
    """
    x = 0
    for _ in range(10):
        x += 1
    print(f"The final value of x is: {x}")
    print(random.randrange(1, 101))


if __name__ == "__main__":
    import random
    do_iteration()

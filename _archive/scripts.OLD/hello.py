#!/usr/bin/env python3
def say_hello(name='Jerry'):
    """Returns a friendly greeting to the named user.
    
    >>> say_hello()
    'Hello Jerry'

    >>> say_hello("Jack")
    'Hello Jack'

    >>> say_hello(123)
    Traceback (most recent call last):
    ...
    TypeError: Can't convert 'int' object to str implicitly
    """
    return "Hello " + name

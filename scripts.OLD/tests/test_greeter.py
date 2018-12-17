import unittest
from greeter import greet

class TestGreetings(unittest.TestCase):
    def test_something(self):
        greet()
        greet()
        greet()
        return True

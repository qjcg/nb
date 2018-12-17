#!/usr/bin/env python3
def greet():
    print("Greetings!")

print('__name__ as seen by greeter.py: {}'.format(__name__))

if __name__ == '__main__':
    import hello

    name = 'john'

    hello.say_hello("John")
    name = 'jack'
    hello.say_hello("James")
    hello.say_hello("Steve")


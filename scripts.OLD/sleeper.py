#!/usr/bin/env python3
import time

def say_hello():
    print('hello')

for n in range(5):
    time.sleep(2)
    print("Iteration", n)

say_hello()
say_hello()
say_hello()
say_hello()

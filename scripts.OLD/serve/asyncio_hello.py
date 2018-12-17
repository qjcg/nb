#!/usr/bin/env python3
import asyncio

def print_and_repeat(loop):
    print('Hello World')
    loop.call_later(2, print_and_repeat, loop)

loop = asyncio.get_event_loop()
loop.call_soon(print_and_repeat, loop)
try:
    loop.run_forever()
finally:
    loop.close()

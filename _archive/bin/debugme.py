#!/usr/bin/env python3

import pdb

x = 0

for _ in range(10):
    pdb.set_trace()
    if x == 7:
        print("lucky")

    x += 1

print(f"Final value of x: {x}")

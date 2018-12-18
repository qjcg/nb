#!/usr/bin/env python3
# A simple script to demonstrate profiling.

import time

def funcA():
    print("Running run_fast")

def funcB():
    print("Running run_slow")
    time.sleep(5)

funcA()
funcA()
funcA()

funcB() # PERFORMANCE BOTTLENECK!

funcA()

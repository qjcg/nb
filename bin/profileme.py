#!/usr/bin/env python3
# A simple script to demonstrate profiling.

import time

def run_fast():
    print("Running run_fast")

def run_slow():
    print("Running run_slow")
    time.sleep(5)

run_fast()
run_fast()
run_fast()

run_slow() # PERFORMANCE BOTTLENECK!

run_fast()

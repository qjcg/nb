#!/usr/bin/env python3

import time

@profile
def f1(n: int=3) -> int:
    print("Running SLOW function")
    time.sleep(n)
    return 42

def f2() -> int:
    print("Running FAST function")
    return 43


if __name__ == '__main__':
    f1()
    f1(5)
    f2()
    f1(10)
    f2()

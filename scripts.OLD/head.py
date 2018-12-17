#!/usr/bin/env python3

f = open('/etc/passwd')
for _ in range(10):
    print(f.readline().rstrip())

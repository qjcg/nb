#!/usr/bin/env python3
# Read in a CSV file, store it as a list-of-lists, and print it out.

# SAMPLE INPUT:
#   aaa,bbb,ccc
#
# SAMPLE OUTPUT
# [ ['aaa', 'bbb', 'ccc'], ... ]

data = []

with open('files/test.csv') as f:
    for line in f:
        data.append(line.rstrip().split(','))

print(data)

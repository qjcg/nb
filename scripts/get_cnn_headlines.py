#!/usr/bin/env python3
"""
Retrieve and print all headlines on the front page of CNN.
"""

from splinter import Browser

with Browser('firefox', headless=True) as b:
    b.visit('https://www.cnn.com/')
    headlines = b.find_by_css('.cd__headline-text')
    for h in headlines:
        print(h.text)

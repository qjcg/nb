#!/usr/bin/env python3

import random

stocks = ['AAPL', 'GOOG', 'MSFT', 'RHT']

random.seed(123)
for _ in range(5):
    print(random.choice(stocks))

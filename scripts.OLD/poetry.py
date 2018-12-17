#!/usr/bin/env python3

import random
import sys

articles = ["The", "A", "An"]
subjects = ["Snowden", "Caliphate", "Badguys", "BlackOps"]
verbs = ["swatted", "suicided", "moved (to russia)"]
adverbs = ["superbly", "quietly", "vengefully", "patriotically"]

num = int(sys.argv[1])

if not 0 < num < 11:
    num = 5

for _ in range(num):
    ar = random.choice(articles)
    su = random.choice(subjects)
    ve = random.choice(verbs)
    if random.randrange(2):
        ad = random.choice(adverbs)
        line = '{} {} {} {}'.format(ar, su, ve, ad)
    else:
        line = '{} {} {}'.format(ar, su, ve)

    print(line)

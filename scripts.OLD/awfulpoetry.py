#!/usr/bin/env python3

import random
import sys

articles = ['A', 'The']
subjects = ['Snowden', 'Putin', 'Harper', 'badguys', 'blackops']
verbs = ['hacked', 'infiltrated', 'slept', 'jumped', 'pentested']
adverbs = ['sheepishly', 'furiously', 'awfully', 'magnanimously']

iterations = 5
if len(sys.argv) > 1:
    iterations = int(sys.argv[1])
    if 0 >= iterations or iterations > 10:
        iterations = 5

for _ in range(iterations):
    ar = random.choice(articles)
    su = random.choice(subjects)
    ve = random.choice(verbs)
    if random.randrange(2):
        ad = random.choice(adverbs)
        print(ar, su, ve, ad)
    else:
        print(ar, su, ve)

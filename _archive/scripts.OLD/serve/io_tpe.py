#!/usr/bin/env python3
import concurrent.futures as cf
import random

import requests

URLS = ['http://api.icndb.com/jokes/random/',
        'http://news.google.ca',
        'http://news.ycombinator.com',
        'http://www.savoirfairelinux.com',
        'http://www.python.org'
]

def get_jokes(urls):
    for u in urls:
        data = requests.get(u)
        print(data.status_code)
    return True


with cf.ThreadPoolExecutor(max_workers=8) as executor:
    jobs = []
    for _ in range(10):
        job = executor.submit(get_jokes, URLS)
        jobs.append(job)

    for future in cf.as_completed(jobs):
        print('future completed:', future.result())

#!/usr/bin/env python3
import random
from bottle import get, run

@get('/')
def index():
    return {'a': 'dog', 'random_number': random.randrange(101)}

run(host='localhost', port='9898')

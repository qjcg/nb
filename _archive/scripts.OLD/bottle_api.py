#!/usr/bin/env python3

import random

from bottle import get, run


@get('/')
def index():
    return {'num': random.randrange(1, 101)}

run()

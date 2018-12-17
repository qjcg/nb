#!/usr/bin/env python3

import requests
from argparse import ArgumentParser

BASE_URL = 'http://localhost:9999'

parser = ArgumentParser(description='An awesome joke client!')
parser.add_argument('-l', '--list', action="store_true", help='list all jokes')
conf = parser.parse_args()

if conf.list:
    res = requests.get(BASE_URL + '/joke')
    print(res.text)
else:
    print('Not much to do!')

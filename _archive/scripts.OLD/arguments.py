#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='This is a real great CLI tool!')
parser.add_argument('-n', type=int, nargs='?', default=2,
                    help='The number of foos to bar')
parser.add_argument('-l', '--language', 
                    help='The language to speak in')
config = parser.parse_args()

if config.n > 5:
    print('Big number!')
else:
    print('Small number!')

if config.language == 'spanish':
    print('Hola!')
else:
    print('Je ne vous comprends pas.')

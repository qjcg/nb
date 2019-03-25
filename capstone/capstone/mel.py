import sys

from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'))
    parser.add_argument('-d', '--debug', action='store_true',
                        help="debug logging")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        stdin = sys.stdin.readlines()

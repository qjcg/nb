#!/usr/bin/env python3
import concurrent.futures
import requests

URLS = ['http://www.example.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://www.test.com'] * 3

# Retrieve a single page and report the url and contents
def load_url(url):
    res = requests.get(url)
    return res.content.decode()

nbytes_list = [load_url(url) for url in URLS]
#for n in nbytes_list:
#        print('page is %s bytes' % (n.decode()))

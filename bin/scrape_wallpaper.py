#!/usr/bin/env python3
# Scrape wallpapers from hdwallpapers.net

import sys

import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html5lib')
for img in soup.select('img.thumbnail-img'):
    print(img['src'])

print("howdy")

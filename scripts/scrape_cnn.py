#!/usr/bin/env python3
"""Scrape headlines from CNN
"""

import requests
from bs4 import BeautifulSoup

cnn = requests.get("https://www.cnn.com/").body
soup = BeautifulSoup(cnn)
headlines = soup.select('article .cd__headline_text')
for h in headlines:
    print(h)

#!/usr/bin/env python3
# Get wallpapers from hdwallpapers.net

# Standard Library imports
import sys

# Third party imports
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]

# Do HTTP request
res = requests.get(url)

# Parse HTML
soup = BeautifulSoup(res.text, "html5lib")

# Loop through all found images and print URLs to stdout.
for img in soup.select('img.thumbnail-img'):
    print(img['src'])

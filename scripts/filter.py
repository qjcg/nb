#!/usr/bin/env python3
"""An example of a unix command line filter script.
"""

import sys

for l in sys.stdin:
    print(l.rstrip().upper())

#!/usr/bin/env python3

import re
import sys

for line in sys.stdin:
    digits = re.sub('\D', '', line)
    if len(digits) == 10:
        print('({}) {}-{}'.format(digits[:3], digits[3:6], digits[6:]))

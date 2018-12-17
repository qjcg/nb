#!/usr/bin/env python3

import re
import sys

RE_VALID_PHONE = re.compile(
                    #'^\s*(\(\d{3}\)|\d{3})( |-)?\d{3}( |-)?\d{4}\s*$'
                    '^\s*\(?'
                    '(?P<area>\d{3})'
                    '\)?( |-)?'
                    '(?P<n1>\d{3})'
                    '( |-)?'
                    '(?P<n2>\d{4})'
                    '\s*$'
                 )

for line in sys.stdin:
    m = RE_VALID_PHONE.search(line.rstrip())
    if m:
        print('({}) {} {}'.format(
                m.group('area'),
                m.group('n1'),
                m.group('n2')))
    else:
        print("ERROR ERROR ERROR!!")

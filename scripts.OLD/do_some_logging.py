#!/usr/bin/env python3
import logging
import sys

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    logging.basicConfig(level=logging.DEBUG, filename='/tmp/test.log',
                        format='%(asctime)s ' + sys.argv[0] + ' %(levelname)s: %(message)s')
else:
    logging.basicConfig(level=logging.INFO)

logging.debug('debug debug debug')
logging.info('info info info')
logging.warning('warning warning warning')

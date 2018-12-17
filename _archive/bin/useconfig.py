#!/usr/bin/env python3
# Demonstrate the use of a YAML config file.

import yaml

with open('files/config.yml') as f:
    config = yaml.load(f)

if config['debug_mode']:
    print("We're in DEBUG MODE")

config['new_param'] = ['aaa', 'bbb', 'ccc']

with open('/tmp/config.yml', 'w') as f:
    yaml.dump(config, f)

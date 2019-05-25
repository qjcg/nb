#!/usr/bin/env python3
"""Example of using argparse
"""

import argparse

parser = argparse.ArgumentParser(description="A little server command")
parser.add_argument('--ip', '-i', type=str, default='127.0.0.1',
                    nargs='?', help='IP address')
parser.add_argument('--port', '-p', type=int, default=9999,
                    nargs='?', help='Port number')
parser.add_argument('--action', '-a', type=str, default='GET',
                    nargs='?', choices=['GET', 'POST'], help='action')

args = parser.parse_args()

print(f"Starting server on {args.ip}:{args.port}")
print(f"Performing action {args.action}")

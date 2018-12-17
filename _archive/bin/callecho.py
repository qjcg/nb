#!/usr/bin/env python3
# Call the "echo" subprocess from within Python

import sys
import subprocess

argument = sys.argv[1]
p = subprocess.run(["echo", argument], stdout=subprocess.PIPE)

if p.returncode != 0:
    print("echo FAILED")
else:
    print("echo SUCCEEDED")
    print("stdout: {}".format(p.stdout))



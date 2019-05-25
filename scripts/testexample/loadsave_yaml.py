#!/usr/bin/env python3
"""Example of loading and saving YAML data.
"""

import yaml

data = {
    "name": "John Gosset",
    "id": 42
}

print("Saving our data to disk as YAML...")
with open("/tmp/data.yml", "w") as f:
    yaml.dump(data, f)

print("Adding some NEW data")
data["foo"] = "bar"

print("Printing updated data")
print(data)

print("Read back YAML from disk, restoring original data...")
with open("/tmp/data.yml") as f:
    data = yaml.load(f)

print("Printing restored data")
print(data)

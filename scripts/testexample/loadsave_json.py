#!/usr/bin/env python3
"""Example of loading and saving JSON data.
"""

import json

data = {
    "name": "John Gosset",
    "id": 42
}

print("Saving our data to disk as JSON...")
with open("/tmp/data.json", "w") as f:
    json.dump(data, f)

print("Adding some NEW data")
data["foo"] = "bar"

print("Printing updated data")
print(data)

print("Read back JSON from disk, restoring original data...")
with open("/tmp/data.json") as f:
    data = json.load(f)

print("Printing restored data")
print(data)

#!/usr/bin/env python3
"""Example of loading and saving pickled data.
"""

import pickle

data = {
    "name": "John Gosset",
    "id": 42
}

print("Saving our data to disk as a python pickle...")
with open("/tmp/data.pickle", "wb") as f:
    pickle.dump(data, f)

print("Adding some NEW data")
data["foo"] = "bar"

print("Printing updated data")
print(data)

print("Read back pickled data from disk, restoring original data...")
with open("/tmp/data.pickle", "rb") as f:
    data = pickle.load(f)

print("Printing restored data")
print(data)

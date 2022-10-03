import json

file_path = "data.json"
# some JSON:
with open(file_path) as f:
# parse x:
    data = json.load(f)

# the result is a Python dictionary:

    print(data)
  

import json

# file_path: str = 'data.json'
#
# with open(file_path, 'r') as file:
#     data: dict = json.load(file)
#     print(data)

data: dict = {'name': 'Bob',
              'age': 43,
              'job': None}

with open('new_json.json', 'w') as file:
    json.dump(data, file)

#truthy and falsy
print(bool([]))
print(bool([None]))
print(bool(None))
print(bool(200))

users: dict = {1: 'Mario', 2: 'Luigi', 3: 'James'}
# users: dict = {}

if users:
    for k, v in users.items():
        print(k, v, sep=':  ')
else: print('No Data Found')

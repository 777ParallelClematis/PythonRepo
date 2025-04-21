a: int = 200 #assignment operator
b: int = 200

print(a == b) #do not use 'is' here ---- that checks for IDENTITY, not value

var: int | None = None
if var is None:
    print('There is no var')
else:
    print(f'var is {var}')
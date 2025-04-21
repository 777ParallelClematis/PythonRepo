number: int = 2

if number > 0:
    result: str = 'Above 0'
else:
    result: str = '0 and below'
print(result)

#or this can be shorthanded with:
result: str = 'Above 0' if number > 0 else '0 and below'

print(result)
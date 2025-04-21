a: float = 200.234234
b: float = 18.1231233
c: float = 47.3242834

result: float = a + b + c
rounded: float = round(result, 2)
print(rounded)

print(round(result, 1))
print(round(result, 2))
print(round(result, 0))
print(round(result, -1))
print(round(result, -2))
#exec()
#does not return anything, executes code

code: str = """
x:int=10
y:int=20

print(x+y)
print('Hello, World!')

for i in range(3):
    print(i)

"""
exec(code)

while True:
    user_input: str = input('Command: ')
    exec(user_input)

#obv don't use this online
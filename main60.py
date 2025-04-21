fruit: str = 'apple'
number: int = 10

def funct() -> None:
    print('funct() was called!')

print (f'callable(): {callable(fruit)}') #not callable
print (f'callable(): {callable(funct)}') #is callable


if callable(funct):
    funct()
else:
    print('Object is not callable')
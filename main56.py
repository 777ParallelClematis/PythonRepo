print(locals())
print(globals())

EXAMPLE: str = 'Bob'

def add(a: int, b: int) ->None:
    result: int = a + b
    print(f'{a}+{b}={result}')

    print('add() has:', locals())
    print('add: can see:', globals())

add(1, 1)
#returns: add() has: {'a': 1, 'b': 1, 'result': 2}
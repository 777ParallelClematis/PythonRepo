from enum import nonmember

print(1, 2, 3, 4, 'hello', sep=':')

def add(*args: int) -> int: #adds 'all' args
    print(args)
    return sum(args)

print (add(1,2,3))

def greet(greeting: str, *people:str, ending:str) -> None:
    for person in people:
        print(f'{greeting}, {person}{ending}')

greet('Hello', 'Brenda', 'Jess', ending='!')

#keyword arguments

#converts into a dictionary
def pin_position(**kwargs: int) -> None:
    print(kwargs)
pin_position(x=10, y=3)

def func(*args: str, default: int, **kwargs: int)-> None:
    print(args)
    print(kwargs)
    print(default)
func('a', 'b', default=20, a=1, b=2)


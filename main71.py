a, b, c = 5, 10, 12 #another way to assign values to variables

print(a, b)

c, d = 'XY'
print(c, d) # returns:    X Y

e, *f = 'abcdef'
print(e,f) #f gets all values apart from the value of 'a'


def add(a: int, b: int) -> None:
    print(f'{a+b =}')

add(5,10) #a+b =15
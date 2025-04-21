numbers: list[int] = [1,2, 3, 4, 5]

def double(number: int) -> int:
    return number * 2

doubled: map = map(double, numbers)
print(doubled) #prints the map object
print(list(doubled)) #prints the doubled list

doubled: map = map(lambda n : n * 2, numbers)
print(doubled) #prints the map object
print(list(doubled)) #prints the doubled list

letters: list[str] = ['a', 'b', 'c']
def combine_elements(n: int, l:str) -> tuple[int, str]:
    return n, l

combined: map = map(combine_elements, numbers, letters)
#combined: map = map(lambda n, l: (n, l), numbers, letters)
print(list(combined)) # returns: [(1, 'a'), (2, 'b'), (3, 'c')] -- stops when one list runs out


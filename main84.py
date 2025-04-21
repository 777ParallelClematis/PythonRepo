from typing import Generator

def five_numbers() -> Generator:
    for i in range(1, 6):
        yield i

numbers: Generator = five_numbers()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

#they are exhaustive, once they're generated they disappear

print(list(numbers)) #shows whats left

#good for working with big bits of data

def huge_data() -> Generator:
    for i in range(1, 100_000_000_000):
        yield i

data: Generator = huge_data()
print(next(data))
print(next(data))
print(next(data))
print(next(data))
numbers: list[int] = list(range(1, 21))
print(numbers)

# def is_even(number: int) -> bool:
#     return number % 2 ==0

# even_numbers: filter = filter(is_even, numbers)
# print(even_numbers)
# print(list(even_numbers))

even_numbers: filter = filter(lambda n: n % 2 == 0, numbers)
print(even_numbers)
print(list(even_numbers))

#another example

people: list[str] = ['Anna', 'Bob', 'Betty', 'James', 'John']
long_names: filter = filter(lambda name: len(name) > 4, people)
print(list(long_names))

ln: list[str] = [name for name in people if len(name) > 4]
print(ln)
#filter is memory efficient, list comprehension not so much
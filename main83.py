from typing import Callable

p = lambda x: print(x)
p(10)
p('Hello')

add = lambda a, b: a + b
print(add(5, 11))

def use_all(f: Callable, values: list[int]) -> None:
    for value in values:
        f(value)

use_all(lambda v: print(f'{v * 'X'}'), [2, 4, 10])

names: list[str] = ['Bob', 'James', 'Samantha', 'Luigi', 'Joe']
sorted_names: list[str] = sorted(names, key=lambda x: len(x))
print(sorted_names)
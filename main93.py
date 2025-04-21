from timeit import timeit

# Using the ** operator
power_time: float = timeit('a**b', setup='a, b = 10, 3')
print(f'a**b: {power_time:.6f}s')

# Using math.pow
math_power_time: float = timeit('pow(10, 3)', setup='from math import pow')
print(f'math.pow: {math_power_time:.6f}s')

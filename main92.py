from timeit import timeit, repeat

a: str = 'list(range(100))'
b: str = 'list(range(100))'
c: str = 'set(range(100))'

# warmup: float = timeit(stmt=a, number=100_000)
# warmup: float = timeit(stmt=b, number=100_000)
#
# a_time: float = timeit(stmt=a, number=100_000)
# b_time: float = timeit(stmt=b, number=100_000)
#
# print(f'a: {a_time:.3f}s')
# print(f'b: {b_time:.3f}s')

a_time: list[float] = repeat(stmt=a, repeat=5, number=100)
b_time: list[float] = repeat(stmt=b, repeat=5, number=100)

print(a_time)
print(b_time)
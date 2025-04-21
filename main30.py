from math import isclose

a: float = 99.9
b: float = 100

print (f'{a} == {b}?', isclose(a,b, rel_tol=0.1))
print (f'{a} == {b}?', isclose(a,b, abs_tol=0.1))
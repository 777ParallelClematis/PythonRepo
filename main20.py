# asterisks and signatures

# def func(var_a: str, *, var_b:str) -> None:
#     print(var_a)
#     print(var_b)
# func(var_a='a', var_b='b')
#
# def func(var_c: str, /, var_d) -> None:
#     print(var_c)
#     print(var_d)

def func(var_a: str, /, var_b: str, var_c:str) -> None:
    print(var_a)
    print(var_b)
    print(var_c)
func('a', 'b', var_c='c')
func('a', var_b='b', var_c='c')
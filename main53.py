elements: list[str] = ['A', 'B', 'C']
# i: int = 0
#
# for element in elements:
#     i += 1
#     print(f'{i}: {element}')

# enumeration: enumerate = enumerate(elements, start=1)
# print(enumeration)
# print(list(enumeration))

for i, element in enumerate(elements, start=1):
    print(f'{i}: {element}') #or go i+1 here, instead of specifying start=1

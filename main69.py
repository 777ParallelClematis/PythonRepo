big_number : float = 123456789
print(f'{big_number:,}') #formats with comma
print(f'{big_number:_}') #formats with underscore - only these two symbols work for this


fraction: float = 1234.5678
print(f'{fraction:.2f}') #rounds to two dp

var: str = 'BOB'
print(f'{var:10}: Hello') #makes BOB occupy 10 spaces
print(f'{var:>10}: Hello') #makes BOB occupy 10 spaces - now right aligned
print(f'{var:^10}: Hello') #makes BOB occupy 10 spaces - now centre aligned
print(f'{var:$>10}') #empty space is filled with the chosen symbol

numbers: list[int] = [1, 100, 1000, 10000]
for number in numbers:
    print(f'{number:_>5}: counting')
    # returns
    # ____1: counting
    # __100: counting
    # _1000: counting
    # 10000: counting

#path: str = ('\\Users\\ec\\documents\\') #inefficient
path: str = r'\Users\EC\Documents'
print(path)

#can also combine with f strings, so:
user: str = 'EC'
path: str = fr'\Users\{user}\Documents'
print(path)
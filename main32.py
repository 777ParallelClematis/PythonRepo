def outer_func() -> None:
    name: str = ' '
    value: int = 0

    def inner_funct() -> None:
        nonlocal value, name
        name = 'Tom'
        value = 100
    inner_funct()
    print(name, value)

outer_func()
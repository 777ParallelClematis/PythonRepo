#introduced in python 3.8, walrus operator:    :=

def description(numbers: list[int]) -> dict:
    # n_length: int = len(numbers).   we removed this for the walrus operator
    # n_sum: int = sum(numbers)
    # n_mean: float = n_sum / n_length

    details: dict = {
        'length': (n_length := len(numbers)), #walrus creates the variable AND returns the result
        'sum': (n_sum := sum(numbers)),
        'mean': n_sum/n_length
    }

    return details

def main() -> None:
    numbers: list[int] = [1, 10, 5, 200, -4, 7]
    print(description(numbers))
    print(x := 1 > 0) # a demo of what it does, returns True
    #so at the same time, its assigning the value to x and also returning the result

    items: dict[int, str] = {1: 'Cup', 2: 'Chair'}
    if item := items.get(3):
        print(f'You have: {item}')
    else:
        print('No item found')

if __name__ == '__main__':
    main()


#walrus operator is considered controversial amongst developers
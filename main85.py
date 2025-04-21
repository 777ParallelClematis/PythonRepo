status: int = 200

match status:
    case 200:
        print('Connected')
    case 403:
        print('Forbidden')
    case 404:
        print('Not found')
    case _:
        print('Unknown')

while True:
    user_input: str = input('Enter a command: ')
    command: list[str] = user_input.split()
    print(command)

    match command:
        case'find', *images:
            print(f'Finding {images}')
        case'enlarge', image, amount:
            print(f'You enlarged {image} by {amount}')
        case'rename', image, new_name if len(new_name) >3:
            print(f'"{image}" was renamed to "{new_name}')
        case 'download', *images:
            print(f'Downloading: {images}...')
        case 'x' | 'delete', *images:
            print(f'Deleting: {images}...')
        case _:
            print('Command not found...')
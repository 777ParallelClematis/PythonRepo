def get_length(text:str) -> int:
    print(f'Getting the length of "{text}" ...')
    return len(text)
name: str = 'Maria'
length: int = get_length(name)
print(length)

def make_upper(text: str) -> str:
    return text.upper()
print(make_upper('hello'))

#self documenting code, good habit to keep:
#doesnt return anything
def connect_to_internet() -> None:
    print('Connecting to internet...')
print(connect_to_internet())


def greet(name: str, language:str, default : str = 'Hello'):
    if language == 'it':
        print(f'Ciao, {name}!')
    else:
        print(f'{default}, {name}!')

greet('Sophia', 'it', 'Hello')
# or be more explicit
greet(name="Sophia", language='it')
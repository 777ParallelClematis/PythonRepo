from enum import Enum

class State(Enum):
    OFF: int = 0
    ON: int = 1

state: State = State.OFF

if state == State.ON:
    print('The device is turned on')
elif state == State.OFF:
    print('The device is turned off')
else:
    print('Unknown input')


class Color(Enum):
    RED: str = 'R'
    GREEN: str = 'G'
    BLUE: str = 'B'

red: Color= Color.RED
print(red)
print(red.value)
print(red.name)
print(Color('R'))

def buy_car(brand: str, color: Color):
    if color == color.RED:
        print(f'You bought a smoking hot red {brand}')
    elif color == color.GREEN:
        print(f'You bought a chill green {brand}!')
    elif color == color.BLUE:
        print(f'You bought a smooth blue {brand}')
    else:
        print('Unknown color.')

def main() -> None:
    buy_car('BMW', Color.BLUE)
    buy_car('Volvo', Color.RED)
    buy_car('Toyota', Color.RED)
    buy_car('Mercedes', Color.GREEN)



if __name__ == '__main__':
    main()
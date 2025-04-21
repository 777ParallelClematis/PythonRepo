from dataclasses import dataclass

@dataclass

class Coin:
    name: str
    value: float
    id: str

def main() -> None:
    bitcoin: Coin = Coin('Bitcoin', 10_000, 'BTC')
    bitcoin2: Coin = Coin('Bitcoin', 10_000, 'BTC')
    Ripple: Coin = Coin('Ripple', 200, 'BTC')

    print(bitcoin)
    print(Ripple) #being a dataclass means that this prints nicer to the console
    print(bitcoin == Ripple) #always returns false
    print(bitcoin == bitcoin2)  # is the same, its checking the values

if __name__ == '__main__':
    main()
class Calculator:
    def __init__(self, version: int) -> None:
        self.version = version
    @staticmethod
    def add(self, *numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> int:
        return 10


def main() -> None:
    #calc: Calculator = Calculator(version=1)
    result: float = Calculator.add(1, 2, 3, 4) #swap to 'calc' for use w line above
    print(result)

if __name__ == '__main__':
    main()
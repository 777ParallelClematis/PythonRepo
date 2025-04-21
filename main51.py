
class Car:
    __YEAR: int = 2000  # class-level constant (still private)

    def __init__(self, brand: str, fuel_type: str) -> None:
        self.__brand = brand
        self.__fuel_type = fuel_type
        self.__var: str = 'red'

    def drive(self) -> None:
        print(f'Driving: {self.__brand}')

    def __get_description(self) -> None:
        print(f'{self.__brand}: {self.__fuel_type}')

    def display_colour(self) -> None:
        print(f'{self.__brand} is "{self.__var.capitalize()}"')

class Toyota(Car):
    def __init__(self, fuel_type:str) -> None:
        super().__init__('Toyota', fuel_type)
        self.var = 100

    def get_year(self) -> int:
        return self.__YEAR


def main() -> None:
    toyota: Toyota = Toyota('Electric')
    toyota.display_colour()
    toyota.get_year()


if __name__ == '__main__':
    main()

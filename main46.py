#inheritance

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def drink(self) -> None:
        print(f'{self.name} is drinking')

    def eat(self) -> None:
        print(f'{self.name} is eating')

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name) #initialising the parent class

    def bark(self) -> None:
        print(f'{self.name}: bark bark!')

    def routine(self) -> None:
        self.eat()
        self.bark()
        self.drink()


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name) #initialising the parent class

    def meow(self) -> None:
        print(f'{self.name}: Meow Meow!')

    def routine(self) -> None:
        self.eat()
        self.meow()
        self.drink()


def main() -> None:
    dog: Dog = Dog('Boomerang')
    cat: Cat = Cat('Snowball')

    dog.bark()
    cat.meow()

    cat.eat()
    dog.eat()

if __name__ == '__main__':
    main()
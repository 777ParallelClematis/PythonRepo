# __repr__
# __str__

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age



    def main() -> None:
        mario: Person = Person('Mario', 27)
        print(mario)

    if __name__ == '__main__':
        main()

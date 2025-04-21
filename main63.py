numbers: list[int] = [1, 10, 5, 3]
sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers) #doesnt return object, sortrs in ascending order

people: list[str] = ['Anna', 'Betty', 'Anabella']
sorted_people: list[str] = sorted(people) #can also go sorted(people, reverse=True)
sorted_names: list[str] = sorted(people, key = lambda x: len(x))
print(sorted_people)#['Anabella', 'Anna', 'Betty'] - ascending alphabetical order (ascii value)
print(sorted_names)#['Anna', 'Betty', 'Anabella']

class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name}={self.weight}kg'

cat: Animal = Animal('Cat', 10)
kangaroo: Animal = Animal('Kangaroo', 50)
dog: Animal = Animal('Dog', 5)


sorted_animals: list[Animal] = sorted([cat, dog, kangaroo], key=lambda animal: animal.weight)
print(sorted_animals) #returns: [Dog=5kg, Cat=10kg, Kangaroo=50kg]
# animals are sorted by their weight
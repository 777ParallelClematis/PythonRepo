#is isinstance() #checks if an object is an instance of another instance

number: int = 10
pi: float = 3.14
text: str = 'banana'
my_list: list[int] = [1, 2, 3]

print(isinstance(number, int)) #returns True
# print(isinstance(number, str)) #returns False
# print(isinstance(number, float)) #returns False

print(isinstance(pi, int | float))
print(isinstance(text, int | str))

class Animal:
    pass

class Cat(Animal):
    pass

print(isinstance(Cat(), Animal)) #returns true, cat is a type of animal
print(isinstance(Animal(), Cat)) #returns false, animal is NOT a type of cat
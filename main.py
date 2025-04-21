print('hello')  # greets the user
print('hello ' + 'Bob!')
print('hello ' + 'Cat!')
print('hello ' + 'Dave!')

greeting = "Hello"

print(greeting + ' Bob!')
print(greeting + ' Cat!')
print(greeting + ' Dave!')

VERSION = 2  # constant declared in all caps, no true way of declaring constants
PI = 3.1415  # suggests to other devs that it should never be changed
print(VERSION)
print(PI)
# print(10 + 'hello') #doesnt work, incompatible types

# data types

# numeric types
number = -100
percent = 1.5  # called a float
print(type(percent))  # prints <class 'float' in console>
imaginary = 9j

# boolean types
is_connected = True
has_money = False

# string types
text = "hello, bob"

# sequence types
# containers that contain values
numbers = [1, 2, 3, 4]
coordinates = (2.5, 1.0)  # twople

# mapping types
users = {'Mario': 1, 'Luigi': 2}  # dictionary

# set types
raffle = {1, 10, 25, 50}  # a set. can remove and add elements
frozen = frozenset({1, 2, 3})  # cannot modify the set

number = 'Hello'
print(number)
print(type(number))

number: int = 10  # very explicit way of defining variable. will always be int, will give warning
text: str = 'Hello'  # another way
# type hints

age: int = 30
money: int = 100
self_esteem: int = -50

a: int = 5
b: int = 10
print(a + b)
print(type(a / b))

height_in_metres: float = 1.72

number: float = 10 #10.0
# number2: int = 1.0 <-- not happy, doesnt work

print(5 // 3) #returns it as rounded, this gives 1, as to 1dp
print(5 / 3)

print (2 ** 3) # 2 to the power of 3
print (3 % 2 ) #gives the remainder after division

print(10+10 *2) #30
print((10 + 10) * 2)

x: int = 2
x = x + 2
print(x)

#or you can also write

x += 2
print(x)

#comparison operators

a: int = 1
b: int = 5
c: int = 10
d: int = 10

print(a == b) #prints false
print(c == d) #prints true

#or you can check the inverse for 'not'

print(a != b) #prints true
#greater than / less than
print(b > a) #prints true

print (c <= d) #c is less than or equal to d
print (a > b > c) #chaining them works, this returns false

print(c == d and b > a) # both of these must be true to return true
print(c == d or b > a) # returns true if at least one of the conditions are true, which it does

print(not ( a > b)) #returns true, a is Not greater than b
print(not (c ==d)) #returns false

#strings
#can use either '' or ""
name: str = 'Mario' # 'Mario\'s'
fruit: str = "Banana"

poem: str = """
Here I can write anuthing 
in a big chunk
just apart from 
quotation marks
"""
#triple quotation

#converting types

txt_value: str = '100'
int_value: int = 50

print(int(txt_value)+int_value) #returns 150
#you're converting the text value into an int, so they can be added. That can all be done in one 'function' as shown above


print (str(int_value) + txt_value) #returns 50100

print(5.5 +1) #turns it all into a float
print(type(5+5.1)) #returns type float

# print(int('ten')) #gives a value error

print('Welcome to your simple adder!')
#a: str = input('Enter a value for a')
#b: str = input('Enter a value for b')

print('The result is:', int(a) + int(b))


# booleans

is_connected: bool = True
has_money: bool = False

print(10 > 5)

print(int(True)) #returns 1

print(True + True )#returns 2)

# lists

my_list: list = [1,True,'text',[1,2,3]]

people: list[str] = ['Bob', 'James', 'Tom']
print(people[0]) #index zero for Bob
print('Original:', people)

people.append('Jeremy')
print('Original:', people)
people.remove('Bob')
print('Original:', people)

people.pop()
print('Original:', people)
#reassigning
people[0] = 'Charlotte'
print('Original:', people)

people.insert(1, 'Timothy')
print('Original:', people)

people.clear()
print(people) #clears the list

items: tuple = 1, True, 'text'
print(type(items)) #returns tuple
# it is the comma that creates the tuple, not the parenthesis
#cannot be modified after creation

# how about an empty tuple?

new_tuple: tuple = ()
print(type(new_tuple)) #just like this, this prints as type tuple

coordinates: tuple[float, float] = 1.5, 2.5
print(coordinates)

#sets => no guaranteed order

elements: set = {99,True, 'Bob'}
print(elements) # prints different order

#add elements
elements.add('James')
print(elements)

#remove elemnets
elements.remove('Bob')

#removes random element
elements.pop()

elements.clear()

#frozen sets
#immutable, memory efficient, does not change
#if your data isn't going to change later

things: frozenset = frozenset({99, 1, 2, 3})
#it removes duplicates
print(things)

#key value pair structure - a dictionary
#retrieving data often comes like this

users: dict = {1: 'Bob', 2:'Luigi'}
print(users)
print(users[2])
users[3] = 'Mario'
users.pop(2)

print(users)

weather: dict = {'time': '12:00',
                 'weather': {'morning': 'rain', 'evening':'more rain'}}
print(weather)
print(weather['time'])
print(weather['weather']['morning']) #accessing a nested dictionary

# None type, represents nothing.

no_value: None = None
print(no_value)
print(type(no_value))

users: dict = {1: 'Mario', 2: 'Luigi'}
print(users.get(3))

#union type
possible_user: str | None = users.get(2)
print(possible_user)
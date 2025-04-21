text: str = 'Hello World'
for i in range(3):
    print(text)
#to see the list
for i in range(10):
    print(f'{i}:{text}')
#with a list
people: list[str] = ['Bob', 'James', 'Maria']
for person in people:
    print(person)

#with more stuff
for person in people:
    if len(person) >4:
        print(f'{person} has a long name')
    else:
        print(f'{person} has a short name')



numbers: list[int] = [1, 2, 3]

doubled: list[int] = []
for number in numbers:
    doubled.append(number*2)
print(doubled)

#this is a lot of code for something simple
#list comprehension

double_lc: list[int] = [number * 2 for number in numbers]
print(double_lc)

names: list[str] = ['Maria', 'Luisa', 'Joanna']
j_names: list[str] = []

for name in names:
    if name.startswith('J'):
        j_names.append(name)
print(j_names)

#shorten it
j_names_lc: list[str] = [name for name in names if name.startswith('J')]
print(j_names_lc)
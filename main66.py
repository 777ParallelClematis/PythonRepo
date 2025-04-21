#zip()
numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ['A','B','C','D']
symbols: list[str] = ['!','$','*','^']

#we want to combine these

zipped: zip = zip(numbers, letters) # can add symbols too, why notttt
#zipped: zip = zip(numbers, letters, strict=True) -------- this here ensures they are the same length
print(zipped)
print(list(zipped)) #[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]


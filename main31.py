number: int = 999

def change_number() -> None:
    global number
    number = 10 #local variable, grab it from the outer source

print(number)
change_number()
print(number)

#prints 999 and then 10
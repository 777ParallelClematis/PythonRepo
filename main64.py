#eval() #evaluate, pass anything through it


result: int = eval('1+10+100')
print(result) #returns 111

x: int = 5
y: int = 10
 #returns 15

while True:
    user_input: str = input('Enter math: ')
    print(eval(user_input))
#on entering '1+2' in terminal on running, this returns '3'

#eval is dangerous because users can really enter anything into the program
#people can make an injection from this
#i.e, in commandline you can write 'print('hello')' and it will print hello
#
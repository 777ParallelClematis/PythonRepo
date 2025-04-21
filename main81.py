#pip install mypy
#then in settings, go to plugins and find mypy, install/apply it
items: list[str] = ['cup', 'apple', True, [1,2,3]] #obv NOT right, its an issue that only mypy brings up

#run 'mypy (filename).py' in terminal to check its been annotated right

def func(default: int = None): #mypy isnt happy with this either, brings up an error
    ...

def func2(default: int | None = None): #mypy is cool with this
    ...
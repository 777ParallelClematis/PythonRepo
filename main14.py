#defining a function
from datetime import datetime
import time


def greet():
    print('Hello!')

greet()
greet()
greet()

def show_time():
    now:datetime = datetime.now()
    print(f'time: {now: %H:%M:%S}')

show_time()
time.sleep(2)
show_time()
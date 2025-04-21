import time
from operator import truediv


def connecttointernet(signal: bool, delay: int) -> None:
    if delay > 5:
        signal = True
    if signal:
        print('Connected!')
    else:
        print(f'Connection failed. Try again in {delay}s...')
        time.sleep(delay)
        connecttointernet(signal, delay+2)

connecttointernet(False, 0)
import time

connected: bool = True

while connected:
    print('Using Internet')
    time.sleep(5)
    connected = False

print('Connection Ended')
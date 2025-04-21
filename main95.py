from typing import TextIO

file_path: str = 'info.txt'
try:
    file: TextIO = open(file_path, 'r')
    text: str = file.read()

    raise Exception('Unknown Exception...')
    print(text)
except FileNotFoundError:
    print('Could not find the file')
except Exception as e:
    print(e)
finally:
    print('Force closing the file')
    file.close

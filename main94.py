from typing import TextIO

file_path: str = 'info.txt'

file: TextIO = open(file_path, 'r')
text: str = file.read()
print(text)
file.close


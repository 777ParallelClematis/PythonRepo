file_path: str = 'info.txt'

with open('info.txt', 'w') as txt: #wipes the file apart frmo whats added
    txt.writelines(['Eggs\n', 'Ham\n', 'Spam\n'])
    txt.write('Hello!')
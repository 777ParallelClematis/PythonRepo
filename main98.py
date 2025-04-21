file_path: str = 'info.txt'

with open(file_path, 'a') as txt: #APPEND this time
    txt.write('I am some text\n') #this gets sent to info.txt file
#if you refer to a file that doesnt exist, python will create that file
file_path: str = 'info.txt'

with open(file_path, 'r') as f: #raw - read append write
    #text: str = f.read()
    #print(f.read(5)) #get 5 bytes back
    #print(f.read(5)) #get the next 5 bytes
    #print(f.read()) #rest of the info
    print(f.readline(5)) #5 bytes again
    print(f.readline())
    print(f.readline())
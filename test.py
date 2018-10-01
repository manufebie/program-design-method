import os

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files')
file_n = 'pride_and_prejudice.txt'

with open(file_n, 'r') as f:
    chars = f.read()
    content = f.read().split()
    #print(content)

    count = 1

    for c in content:
        count += 1

    numofchars = 1
    for char in chars:
        numofchars +=1
    
    print(numofchars)

    print(count)

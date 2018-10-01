'''
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n 
(where n is the number of lines in the file).
'''

import os

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files')
file_n = 'original_file.txt'

# Read original file
with open(file_n, 'r') as f:
    f_content = f.readlines()
    #print(f_content)
    
    print()
    
    with open('new_copy.txt', 'w') as wf: 
        copy_content = wf.writelines(f_content) # Copy content from the original .txt file
        

with open('new_copy.txt', 'r') as rc:
    print('Copied text file: ')
    read_copy = rc.read().split()
    #print(read_copy)

    counter = 1

    for i in read_copy:
        counter += 1
        new
        print('{} {}'.format(counter, i))
        



     







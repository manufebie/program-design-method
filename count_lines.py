'''
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n 
(where n is the number of lines in the file).
'''

import os

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files') # working directory
file_n = 'pride_and_prejudice.txt' # filename
count = 0

with open(file_n, 'r') as f: # open file in readmode 

    with open('count_lines.txt', 'w') as fw: # open file in write mode
        
        for line in f: # iterate over each line from file to read from
            count += 1 # Count the number of lines
            copy = fw.write('Line {}: {}'.format(count, line)) # format the string

    
    




     







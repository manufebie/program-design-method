'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, 
the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. 
Make sure your program ignores capitalization.
'''

import os, sys, string

from collections import Counter

# set filepath to the directory I want to read file from
file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files')
file_n = 'pride_and_prejudice.txt'

with open(file_n, 'r') as f:
    '''
    Using a context manager to open a file so it's only opened inside the with block 
    '''
    f_contents = f.read().lower()
    f_contents = Counter(f_contents.split()) 
    print(f_contents)
    print()
    
    print('Unique words: \n')
    
    for w in f_contents: # Iterate through every word inside f_contents 

        if  f_contents[w]== 1:
            print('{}: occurs {} time'.format(w, f_contents[w]))

    print()
    total = sum(f_contents.values())
    print('Total words: {}'.format(total))


            

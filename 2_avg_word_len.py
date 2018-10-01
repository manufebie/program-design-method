'''
Write a program that will calculate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
'''

import os

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files')
file_n = 'pride_and_prejudice.txt'


with open(file_n, 'r') as f:
    f_content = f.read()
    char_count = len(f_content) # Total number of characters
    word_count = len(f_content.split()) # total number of words
    avg = char_count // word_count # Divide num of chars with num of words 

    # print out result
    print('Char total: {}'.format(char_count))
    print('Word toal: {}'.format(word_count))
    print('Average word length: {}'.format(avg))


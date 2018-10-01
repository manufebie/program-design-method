'''
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except that  . Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
a.	Periods followed by a digit with no intervening whitespace are not sentence boundaries.

b.	Periods followed by whitespace and then an upper case letter,  but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.
c.	Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, www.aptex.com, or e.g).
d.	Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file can write its content with each sentence on a separate line
'''

import os

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files') # path destination
file_n = 'mr_miyagi.txt' # file to read and copy from
boundaries = ['.', '!', '?']
exceptions = ['Mr.', 'Mrs.', 'Dr.', 'Jr.']
copied_text = ''

with open(file_n, 'r') as fr: # Open original in read mode
    f_content = fr.read().split()
    # print(f_content)

    with open('resentence.txt', 'w') as fw: # write the contents of the original file into the new one
        
        for word in f_content: # loop through words from original file
            line = word + ' '
            if word.endswith(boundaries[0]) or word.endswith(boundaries[1]) or word.endswith(boundaries[2]):
                # Should show ignore the exceptions
                line += '\n'

            copied_text += line
        print(copied_text)
        c_to_f = fw.write(copied_text)
        
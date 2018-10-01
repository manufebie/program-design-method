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

file_path = os.chdir('/home/manu/Desktop/computer_science/semester1/exercises/program_design_methods/files/text_files')
file_n = 'mr_miyagi.txt'

with open(file_n, 'r') as fr:
    # Open original file to read from

    with open('resentence.txt', 'w') as fw:
        # write the contents of the original file into the new one
        for line in fr:
            new = line.split('.') # use split to split lines
            print(''.join(new))
            #print(new)
            fw.write(line)

    
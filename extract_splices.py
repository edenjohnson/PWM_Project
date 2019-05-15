# extract_splices.py
# Authors: Eden Johnson
# Last updated: 5/14/19
# Purpose: Obtain the Training data for the PWM
# Program uses: Built-in Python function open() to read and write from a file,
#               built-in Python methods .readlines(), .write(), .close(),
#               .rstrip() and .split().
#               Program also uses variable assignment and extended splice
#               operator.

# input from EI_true.seq
sequence_file = open("EI_true.seq", 'r')
# create a file to write to
nine_file = open("EI_nine.txt", 'w')

# skip the first 4 lines of input file
sequence_lines = sequence_file.readlines()[4:]
# get the DNA sequence isolated 
for line in sequence_lines:
    line_data = line.rstrip("\n")
    # create list of columns
    sequence_info = line_data.split(" ")
    # obtain DNA sequence from the last column, 140 characters long
    dna_seq = sequence_info[-1]
    # extract the 9 characters of the DNA sequence at position 67 to 75
    extracted = dna_seq[67:76]
    # write the extracted characters to EI_nine.txt file
    nine_file.write(extracted + "\n")
     
# close the files
sequence_file.close()
nine_file.close()

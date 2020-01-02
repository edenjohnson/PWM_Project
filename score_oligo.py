###############################################################################
# score_oligo.py
# Author : Eden Johnson
# Last Updated: 5/14/19
# Purpose: To compute the the score of a EI_nine sequences based
#          on the position weight matrix
# Program uses: Built-in Python function open(), float(), str(), list(),
#               built-in Python methods .read(), .split(), .write(), .close().
#               Creation of a funciton, for loop, conditional statement.
#               Use of dictionary. 
###############################################################################

# open file to read PWM from, create list of rows
pwm_file = open("EI_nine_pwm.txt",'r')
pwm = pwm_file.read()[:-1].split('\n')

def get_oligo_score(seq):
    """Function to retrieve values from PWM, calculates the score of
        one sequence. """
    # obtain sequence from DNA sequence file
    seq = seq[0:9]
    # create dictionary with rows of PWM that correspond with their bases
    base_dict = {'A':pwm[0].split(),'C':pwm[1].split(),'G':pwm[2].split(),
                 'T':pwm[3].split()}
    
    # create list of bases ['A','C','G','T']
    base_keys = base_dict.keys()
    base_list = list(base_keys)
    
    # sum score of the position of the table
    score = 0
    for i in range(len(seq)):
        if seq[i] == base_list[0]:
            score += float(base_dict['A'][i])
        elif seq[i] == base_list[1]:
            score += float(base_dict['C'][i])
        elif seq[i] == base_list[2]:
            score += float(base_dict['G'][i])
        elif seq[i] == base_list[3]:
            score += float(base_dict['T'][i])
    # return value of function, round to 3 decimal places
    return ("%.3f" % score)


# open file to write to
score_file = open("EI_nine_output.txt","w")
# open file to obtain 9-character long DNA sequences
seq_file = open("EI_nine.txt","r")

# iterate through the sequences, score them by calling function
for line in seq_file:
    score_file.write(line[0:9] + "\t" + str(get_oligo_score(line)) + "\n")
        
# close the files
pwm_file.close()
score_file.close()
seq_file.close()


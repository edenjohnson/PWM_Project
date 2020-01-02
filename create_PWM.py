###############################################################################
# create_PWM.py
# Author: Eden Johnson
# Last updated: 5/14/19
# Purpose: To create the PWM, calculate the probability of each base occurrence,
#          calculate the normalized values and take the log base 2. 
# Program uses: Built-in Python function open(), len(), range(), str()
#               built-in Python methods .readlines(), .log(), .write(),
#               .close(), import of the math module, creation of a function,
#               for loop, conditional statements, use of a dictionary. 
###############################################################################

# import math module
import math
# open the file to read from and create a list of the sequences
file = open("EI_nine.txt",'r')
seq_list = file.readlines()

# open the file to write to
pwm_file = open("EI_nine_pwm.txt",'w')

# obtain the length of the total amount of sequences for probability
length = len(seq_list)

# create a dictionary to assign values to for base count
bases_dict = {'A':[0]*9, 'C':[0]*9, 'G':[0]*9, 'T':[0]*9}

# create a funciton to count bases at each position
def get_bases(character):
    """ Function serves to get the number of each base at each index. """
    for element in seq_list:
        # iterate over each value of the 9 character sequences
        for i in range(len(element)):
            # if the letter is equal to the input value, increase base count
            if element[i] == character:
                bases_dict[character][i] += 1
    return

# call the function and input each base as an argument
base_list = ['A', 'C', 'G', 'T']
for element in base_list:
    get_bases(element)

# create list of dictionary values to perform required math
dict_values = bases_dict.values()
# isolate each count
for counts in dict_values:
    for values in counts:
        # calculate the probability of each base at each position
        probability = (values+0.1)/(length+0.4)
        # calculate the log odd with base 2 at each position
        log_odd = math.log(probability/0.25,2)
        # round the log_odd values for PWM to 3 decimal places
        rounded_values = "%.3f" % log_odd
        # write the values of the PWM to the text file
        pwm_file.write(str(rounded_values))
        if counts[8] !=values:
            pwm_file.write(" ")
        elif counts[8] == values:
            pwm_file.write("\n")

        
# close the files
file.close()
pwm_file.close()

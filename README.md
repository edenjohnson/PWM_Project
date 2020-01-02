# PWM_Project
The Position Weight Matrix is created based off of training data, or a set of model sequences and is utilized to score any additional sequences and compare it to training data. A higher score output by the PWM tells us that the sequence is relatively similar to the training data. This project was divided into three major parts and files; obtaining the training data itself, creating the PWM with probabilities with pseudo counts and log-odd scores, and finally scoring any given sequence as input and comparing it to the PWM.

### Prerequisites/Assumptions

Python 3+ must be installed on the system running the program. 

1st program to run is extract_splices.py, 2nd program to run is create_PWM.py, and 3rd program to run is score_oligo.py.

EI_true.seq must be present in the same directory as extract_splices.py.
EI_nine.txt must be present in the same directory as create_PWM.py.
EI_nine_pwm.txt must be present in the same directory as score_oligo.py.

## Author

**Eden Johnson** 

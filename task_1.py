# Task 1
# Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
# data are set on the command line when the script is run.
# The script should be launched like this:
# >>python my_task.py 1 * 2

import string
import sys
#Make from list a string without spaces
str = "".join(sys.argv[1:])
#Getting result
print('result = ', eval(str))

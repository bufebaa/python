# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:
# >>python my_task.py add 1 2

import string
import sys
str = sys.argv
#Adding in a string operation from the input
operation = str[1]
assert operation in ['add', 'subtract', 'divide', 'multiply']
#Adding values to the list
iNum = str[2:]
value = 0
#Makinf if statement for every operation
if operation == 'add':
    for i in iNum[:]:
         value += int(i)
elif operation == 'subtract':
    for i in iNum[:]:
        value -= int(i)
elif operation == 'multiply':
    value=1
    for i in iNum[:]:
        value *= int(i)
elif operation == 'divide':
    value=1
    for i in iNum[:]:
        value /= int(i)
#Print result
print("result = {output}.".format(output= value))

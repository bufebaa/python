# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:
# >>python my_task.py add 1 2

import string
import sys
str = sys.argv
#Adding in a string operation from the input
operation = str[1]
flag=True
try:
    assert operation in ['add', 'sub', 'div', 'mul']
except:
    print("The operation isn't found")
    flag = False
#Adding values to the list
iNum = str[2:]
value = 0
#Makinf if statement for every operation
if operation == 'add':
    for i in iNum[:]:
         value += int(i)
elif operation == 'sub':
    for i in iNum[:]:
        value -= int(i)
elif operation == 'mul':
    value=1
    for i in iNum[:]:
        value *= int(i)
elif operation == 'div':
    value=1
    try:
        for i in iNum[:]:
            value /= int(i)
    except:
        print("Invalid numbers(")
        flag = False

if flag:print("result = {output}.".format(output= value))
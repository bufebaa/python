# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF syntax (without
# using regular expressions).

import string
import sys
operations=["+","-"]
number_op=0
flag = True
#Getting our input in a string without spaces
str1 = "".join(sys.argv[1:])
only_digits = str1.split("+"or"-")

for i in str1:
    if i in operations:
        number_op+=1
#If the number of operations and numbers is equal result is true 
if len(only_digits)==number_op-1:
    result = (flag,eval(str1))
    print("result = ", result)
else:
    flag = False
    result = (flag, None)
    print("result = ", result)
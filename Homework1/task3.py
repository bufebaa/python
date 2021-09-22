# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF syntax (without
# using regular expressions).
from argparse import ArgumentParser
def main():
    output = None
    parser = ArgumentParser()
    parser.add_argument("formula", nargs = "+")
    arg = parser.parse_args()
    formula = "".join(arg.formula)
    if (Check_formula(formula)):
        output = eval(formula)
    result = (Check_formula(formula), output)
    print("result =", result)

#Function for checking the formuls is correct(returns True) or incorrect(terurns False)
def Check_formula(expresion):
    operation = ['+', '-']
    prev_element = None
    flag = True
    for el in expresion:
        if not (el.isdigit() or (el in operation and prev_element not in operation)):
            return False
        prev_element = el
    return True

main()
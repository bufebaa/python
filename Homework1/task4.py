# Task 4
from argparse import ArgumentParser

#Getting the input
parser = ArgumentParser()
parser.add_argument("capacity", type = int)
parser.add_argument("weights", type = float, nargs = "+")
arg = parser.parse_args()

count_bar = len(arg.weights)
weight_limit = arg.capacity

#function for counting the maximum weights of bars
def limited_weight(count_bar, weight_limit):
    #returns 0 if there are no bars
    if count_bar == 0:
        return 0
    #if the bar is greater so the result is equal to the weight limit
    elif arg.weights[count_bar - 1] > weight_limit:
        return limited_weight(count_bar - 1, weight_limit)
    else:
    #returns max of cases
        return max(
            limited_weight(count_bar - 1, weight_limit),
            limited_weight(count_bar - 1, weight_limit - arg.weights[count_bar - 1])
            + arg.weights[count_bar - 1])


result = []


for i in reversed(range(count_bar)):
    if limited_weight(i + 1, weight_limit) > limited_weight(i, weight_limit):
        result.append(arg.weights[i])
        weight_limit -= arg.weights[i]
        print("add ",arg.weights[i] )
print("Maximum weight:", sum(result))
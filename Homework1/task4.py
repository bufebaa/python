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
def max_weight(count_bar, weight_limit):
    if count_bar == 0:
        return 0
    elif arg.weights[count_bar - 1] > weight_limit:
        return max_weight(count_bar - 1, weight_limit)
    else:
        return max(
            max_weight(count_bar - 1, weight_limit),
            max_weight(count_bar - 1, weight_limit - arg.weights[count_bar - 1])
            + arg.weights[count_bar - 1])


result = []
for i in reversed(range(len(arg.weights))):
    if max_weight(i + 1, weight_limit) > max_weight(i, weight_limit):
        result.append(arg.weights[i])
        weight_limit -= arg.weights[i]
print("Maximum weight:", sum(result))
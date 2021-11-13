import timeit
import random
import os

def ftask():
    first = 0
    with open('text.txt', 'r') as file:
        for line in file:
            if not line.strip().isdigit(): raise TypeError
            first += int(line.strip())
    print(first)

def stask():
    second=0
    with open('text.txt', 'r') as file:
        line = file.readline()
        while line:
            if not line.strip().isdigit(): raise TypeError
            second += int(line.strip())
            line = file.readline()
    print(second)


def ttask():
    third=0
    with open('text.txt', 'r') as file:
        numbers = (line.strip() for line in file)
        for i in numbers:
            if i.isdigit():
                third += int(i.strip())
    print(third)


with open('text.txt', 'a') as f:
    while os.path.getsize('text.txt')<5242800:
        f.write(str(radint(0, 1000))+'\n')
print(timeit.timeit(ft, number=1000))
print(timeit.timeit(st, number=1000))
print(timeit.timeit(tt, number=1000))


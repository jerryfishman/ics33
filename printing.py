# printing.py
#
# ICS 33 Fall 2022
# Exercise Set 1
#
# There's no need to modify or submit these functions.  Your goal in this
# problem is to write a separate module containing unit tests for them.



def print_range(start, stop, step):
    start = int(start)
    stop = int(stop)
    step = int(step)

    value = start

    while value < stop:
        print(value)
        value += step



def print_reversed(values):
    for value in values:
        print(value[::-1])




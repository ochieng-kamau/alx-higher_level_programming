#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        maximum = my_list[0]
        for iteration in my_list:
            if iteration > maximum:
                maximum = iteration
        return maximum
    else:
        return None

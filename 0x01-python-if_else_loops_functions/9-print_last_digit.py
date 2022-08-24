#!/usr/bin/python3

def print_last_digit(number):
    """Get the str representation of the number"""
    num_str = repr(number)
    """Get the last digit and convert str to int"""
    last_digit = int(num_str[-1])
    print(abs(last_digit), end="")
    return (abs(last_digit))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
context = ""
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    context = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    context = "and is less than 6 and not 0"
else:
    context = "and is 0"

print(f"Last digit of {number} is {last_digit} {context}")

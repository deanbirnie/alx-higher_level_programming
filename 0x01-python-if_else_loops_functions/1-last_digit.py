#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
g5 = "and is greater than 5"
l6n0 = "and is less than 6 and not 0"
i0 = "and is 0"
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} {g5}")
elif last_digit < 6 and not 0:
    print(f"Last digit of {number} is {last_digit} {l6n0}")
else:
    print("Last digit of {number} is {last_digit} {i0}")

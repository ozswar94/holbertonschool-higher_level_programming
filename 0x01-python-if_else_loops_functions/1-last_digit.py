#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
print("Last digit of {:d} is".format(number), end=" ")

if number < 0:
    number %= (-10)
else:
    number %= 10

if number == 0:
    print("{:d} and is 0".format(number))
elif number > 5:
    print("{:d} and is greater than 5".format(number))
else:
    print("{:d} and is less than 6 and not 0".format(number))

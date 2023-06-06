#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0 :
    print("the number is positive".format(number))
elif number == 0 :
    print("the number is 0".format(number))
else:
    print("its a negative number".format(number))

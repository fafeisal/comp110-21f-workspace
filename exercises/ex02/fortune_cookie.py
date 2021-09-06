"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730474766"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
random_number: int = randint(1, 4)

if random_number == 1:
    print("You will find yourself in a pickle, but someone you love will help you!")
else:
    if random_number == 2:
        print("Today will be a day of cheer and good fortune for you!")
    else:
        if random_number == 3:
            print("This week will be filled with profitable returns.")
        else:
            if random_number == 4:
                print("Your day will greet you with a new opportunity, take it!")


print("Now, go spread positive vibes!")

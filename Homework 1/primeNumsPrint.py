################
# Author: Daniel Burger
# Date: 2/23/2019
# This program finds and prints all prime numbers
# between and any given number (but in this case, 0 to 100)
#################

NUMBER = 100 #chosen number to print all prime numbers from 0 to NUMBER

for i in range(100):
    #special cases for 2, 3, 5, and 7
    if ((i == 2) | (i == 3) | (i == 5) | (i == 7)):
        print(i)

    if ((i % 2) != 0): #if i is not divisible by 2
        if ((i % 3) != 0): #if i is not divisible by 3
            if ((i % 5) != 0): #if i is not divisible by 5
                if ((i % 7) != 0): #if i is not divisible by 7
                    if (i != 1): #1 is not a prime number
                        print(i)

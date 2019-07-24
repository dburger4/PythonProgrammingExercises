################
# Author: Daniel Burger
# Date: 2/23/2019
# This program draws a patter of pairs of pound signs that have
# more spaces inbetween them the further down you go
#################

NUM_LINES = 9 # number of lines the code will print

for i in range(NUM_LINES):
    print('#', end='') #prints the first pound sign, always first charcter each line
    for j in range (i):
        print(' ', end='') #prints as many spaces as whatever row it is in (starting with row 0)
    print('#') #prints last pound sign, always last character on each line

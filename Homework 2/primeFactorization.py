################
# Author: Daniel Burger
# Date: 03/04/2019
# This program returns a list of all prime factors in
# a number in ascending order when given any positive integer
#################

def main():
    input_num = input('Enter a number: ') #asks user to enter number
    num = int(input_num) #typecasts input to an int to be used for math

    prime_factors_list = prime_factors(num) #calls function to return list
    print(prime_factors_list) #prints answer

def prime_factors(n):
    prime_nums = [] #creates empty list to store prime factors
    exit_loop = 1 #will become 0 when loop should exit
    
    while exit_loop:
        if (((n%2) == 0) and (n != 2)): #if number is divisible by 2
            n = n / 2 #then divide it by 2
            prime_nums.append(2) #and add 2 to the list of prime factors
            continue
        if (((n%3) == 0) and (n != 3)): #if number is divisible by 3
            n = n / 3 #then divide it by 3
            prime_nums.append(3) #and add 3 to the list of prime factors
            continue
        if (((n%5) == 0) and (n != 5)): #if divisible by 5
            n = n / 5 #then divide by 5
            prime_nums.append(5) #add 5 to list
            continue
        if (((n%7) == 0) and (n != 7)): #if divisible by 7
            n = n / 7 #divide by 7
            prime_nums.append(7) #add 7 to list
            continue
        
        prime_nums.append(int(n)) #add last prime number to list
        exit_loop = 0 #allows while loop to exit

    return prime_nums #returns answer in ascending order (list was built in ascending order)

main()

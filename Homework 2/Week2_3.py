################
# Author: Daniel Burger
# Date: 03/04/2019
# This program determines all natural numbers less than
# or equal to n which are coprime to n as well as the
# result of the Euler's phi function when run on n
#################

def main():
    n = int(input('Enter a natural number: ')) #takes input from user and typecasts it to int

    coprime_nums, phi = totient(n) #calls totient function to get answers
    
    #prints output to user
    print(coprime_nums, end='')
    print(',' + str(phi))
    

def totient(n):
    all_nums = list(range(1,n)) #list of numbers <= n
    #print(all_nums)
    for i in range(1,n): #for every number in all_nums
        coprime = are_coprime(i,n)
        if not coprime: #if the numbers are not coprime
            all_nums.remove(i) #remove the number from the list

    return all_nums, len(all_nums)

#Determines if two numbers are coprime
def are_coprime(x,y):
    x_primes = prime_factors(x) #finds prime factors of x
    y_primes = prime_factors(y) #finds prime factors of y

    x_primes_set = set(x_primes) #converts to set
    y_primes_set = set(y_primes) #converts to set

    difference = x_primes_set - y_primes_set #finds differences in set

    if (difference == x_primes_set): #if true, both sets share no values, aka coprime
        return 1
    else: #not coprime
        return 0

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

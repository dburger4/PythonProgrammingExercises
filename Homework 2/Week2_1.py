################
# Author: Daniel Burger
# Date: 03/04/2019
# This program creates a dictionary of States and capitols
# in the US, and quizzes the user
#################
import random

states_capitals = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','California':'Sacramento','Colorad':'Denver','Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'St. Paul','Mississippi':'Jackson','Missouri':'Jefferson City','Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampsire':'Concord','New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
correct = 0 #initial score
incorrect = 0 #incorrect score
answer = 'capital' #initial answer to enter loop

#Opening line prompint user how to quit
print('Welcome to U.S. States and Capitals quiz! Enter "quit" as your answer to quit.')
print()


while (answer != 'quit') :
    rand_state = random.choice(list(states_capitals))
    print('What is the capital of ' + rand_state +'?') #asks user a question using random state generator
    print('Number of correct responses: ' + str(correct)) #tells user how many they have gotten right
    print('Number of incorrect responses: ' + str(incorrect)) #tells user how many they have gotten wrong
    answer = input('Enter answer here: ') #prompts user to answer

    rand_state_cap = states_capitals.get(rand_state) #finds the correct answer

    if (rand_state_cap == answer): #if answer is correct
        correct = correct + 1 #add a point to correct
        print()
        print("Correct!") #notify the player of their achievement
        print()
    else: #if answer is incorrect
        incorrect = incorrect + 1 #add a point to incorrect
        print()
        print("Incorrect") #notify the player of their failure
        print()

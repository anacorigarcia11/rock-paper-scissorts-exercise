print("Rock, Paper, Scissors ... Shoot!")
# your solution code here!

import random 
#process user input
user_name = input("Welcome! What is your name? ")
print("----")

#welcome
print(f"Welcome to the game of Rock/Paper/Scissors, {user_name}")
print("----")

#user choice
next = input("Choose - Rock, Paper, Scissors: ")
user_choice = next.lower() #knew there were functions in dealing with capitilization so i looked it up on W3Schools

options = ["rock", "paper", "scissors"] #avoiding duplication 

if user_choice not in options:
    print("Oops! That is not a valid option")
else:
    print("----")

    comp_choice = random.choice(options)
    print("You chose " + user_choice)
    print(f"The computer chose {comp_choice}" )
    print("----")
#nested if-statement approach
    if user_choice == comp_choice:
        print("It's a tie! Thank you for playing, hope you had fun :)")
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("You lose! Thank you for playing, hope you had fun :)")
        elif comp_choice == "scissors":
            print("You win! Thank you for playing, hope you had fun :)")
    elif user_choice == "paper":
        if comp_choice == "scissors":
            print("You lose! Thank you for playing, hope you had fun :)")
        elif comp_choice == "rock":
            print("You win! Thank you for playing, hope you had fun :)")
    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("You lose! Thank you for playing, hope you had fun :)")
        elif comp_choice == "paper":
            print("You win! Thank you for playing, hope you had fun :)")
    else:
        print("Oops! That is not a valid option")
    
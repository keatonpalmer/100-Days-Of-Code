# This code sort of works. The game can technically be played, provided that the user enters one of the supported values (0, 1, or 2).

# The solution.py file in the same folder handles unexpected values

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Creates a list for different options
options = [rock, paper, scissors]

# Grabs user input and assigns it to user_choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
int(user_choice)
# Assigns random choice from the options list
computer_choice = random.choice(options)

# Prints out ASCII art corresponding to what the user selected
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)

# Prints out what the computer randomly chose
print("The computer chose:")
print(computer_choice)

# If/elif/else statements to determine who wins.
if user_choice == 0 and computer_choice == options[0]:
    print("It's a draw.")
elif user_choice == "0" and computer_choice == options[1]:
    print("You lose.")
elif user_choice == "0" and computer_choice == options[2]:
    print("You win!")
elif user_choice == "1" and computer_choice == options[0]:
    print("You win!")
elif user_choice == "1" and computer_choice == options[1]:
    print("It's a draw.")
elif user_choice == "1" and computer_choice == options[2]:
    print("You lose.")
elif user_choice == "2" and computer_choice == options[0]:
    print("You lose.")
elif user_choice == "2" and computer_choice == options[1]:
    print("You win!")
else:
    print("It's a draw.")

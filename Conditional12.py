""""
temp = 75

if temp >=80 or temp < 60:
    print("The weather is nice!")
else:
    print("stay indoor!")


forecast = "rain"

if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")


computer_choice = 'scissors'

user_choice = input('Do you want - rock, paper, or scissors? \n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
else:
    print('You lose :(Computer winds :D')
"""

import random

computer_choice = random.choice(['scissors', 'rock', 'scissors'])

user_choice = input('Do you want - rock, paper, or scissors? \n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
else:
    print('You lose :(Computer winds :D')
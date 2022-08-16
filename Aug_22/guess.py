#Initial LIST
from random import shuffle


mylist = [' ', 'O',' ']

def shuffle_list(mylist):
    
    shuffle(mylist)
    return mylist

def player_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1, or 2")

    return int(guess)

#Check Guess
def check_guess(mixed_list,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)
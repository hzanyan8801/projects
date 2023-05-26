import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


# Testng the class
"""die = Die()

print(die.value)

new_value = die.roll()
print(new_value)"""


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()

"""
# Testing the Player class
my_die = Die()

my_player = Player(my_die)

my_player.increment_counter()
print(my_player.counter)
my_player.decrement_counter()
print(my_player.counter)

print(my_player.die.value)
my_player.roll_die()
print(my_player.die.value)"""

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("============================")
        print("🎲 Welcome to Roll the Dice!")
        print("============================")
        while True:
            self.play_round()
            #TODO:implement game over

    def play_round(self):
        #Welcome the user
        print("--------New Round------")
        input("🎲 Press any key to roll the Dice!🎲")

        #Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #Show the values
        print(f"Your dice: {player_value}")
        print(f"Computer die: {computer_value} ")

        #Determine the winner and loser
        if player_value > computer_value:
            print("You won the round 🎉")
            self._player.decrement_counter()  #winner
            self._computer.increment_counter()  #loser
        elif computer_value > player_value:
            print("The computer won this round. 😔 Try again.")
            self._computer.decrement_counter()  #winner
            self._player.increment_counter()    #loser
        else:
            print("It's a tie!")

        #show counters
        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter} \n")


#Create instances
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

#Start the game
game.play()
import random
from os import system
import time

"""This script emules a rock, paper, scissors game generating
    pseudo-random choices; it says if you win, lose or get draw.
    It doesn't accept lower case first letter, can show you instructions
    or just close the game. It's made as first step to a mobile game.
    """


instructions = "Type "'Exit'" to close game; type "'Rock'", "'Paper'", "'Scissors'" to play or "'help'" to view this sentence again. "
options = {"Rock":"Paper", "Paper":"Scissors", "Scissors":"Rock"}

def play():
    print(instructions)
    while True:
        player = input("Write your move:")
        if player == "Exit": break
        elif player == "Help": print(instructions)
        elif player in options: 
            result = draw()
            if options[player] == result: print("You lost")
            elif options[result] == player: print("You won")
            else: print("Draw")
        else: print("Invalid option")
        time.sleep(3)
        system('clear')
            
def draw():
    global options
    selection = random.choice(list(options.keys()))
    print(selection)
    return selection

play()
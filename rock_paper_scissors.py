import random
from os import system
import time



instructions = "Type "'Exit'" to close game; type "'Rock'", "'Paper'", "'Scissors'" to play or "'help'" to view this sentence again. "
options = {"Rock":"Paper", "Paper":"Scissors", "Scissors":"Rock"}
commands = {"Exit": system('exit'), "Help":instructions} 

def play():
    print(instructions)
    while True:
        player = input("Write your move:")
        if player in commands: commands[player]
        elif player in options: 
            result = draw()
            if options[player] == result: print("Ganaste")
            elif options[result] == player: print("Perdiste")
            else: print("Empate")
        else: print("Opción no valida")
        time.sleep(2)
            
def draw():
    global options
    selection = random.choice(options.keys())
    return selection

play()
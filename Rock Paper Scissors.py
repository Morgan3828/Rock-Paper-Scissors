# Rock, paper, Scissors
# By Morgan V.
# Set Values & Import

import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
answer = None
winner = 0

OPTIONS = ( None,
            "Rock",
            "Paper",
            "Scissors")

# Conditional execution


while answer != "no" and answer != "n":

# While Loop
    
    while winner == 0:
        userchoice = int( input("Rock, Paper, or Scissors ? :" +
                                "1 for Rock, 2 for Paper, 3 for Scissors.")
        computer = random.randrange(len(OPTIONS))
        if computer > userchoice:
            winner = 0
        print("The computer chose {}.".format + OPTIONS[computer])
        elif computer < userchoice:
            winner = 1
        elif computer == userchoice:
            winner = 0


    answer = input("Do you want to play again (y/n)? ")
    answer = answer.lower()[0]

                          

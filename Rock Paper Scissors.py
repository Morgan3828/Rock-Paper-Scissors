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

# While Loop

while answer != "no" and answer != "n":    
    userchoice = int( input("  1 for Rock, 2 for Paper, 3 for Scissors. " +
                                " Rock, Paper, or Scissors ? :"))
# Conditional Execution
    computer = random.randrange(len(OPTIONS))
    print("The computer chose {}.".format( OPTIONS[computer]))
        
    if computer == 1 and userchoice == 1:
        tkinter.simpledialog("It's a tie")
        
    answer = input("Do you want to play again (y/n)? ")
    answer = answer.lower()[0]

                          

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
# Randomization AI
    computer = random.randrange(len(OPTIONS))
    print("The computer chose {}.".format( OPTIONS[computer]))
        
# Tie section
    if computer == 1 and userchoice == 1:
        print("It's a Tie! Nobody wins.")

    if computer == 2 and userchoice == 2:
        print("It's a Tie! Nobody wins.")

    if computer == 3 and userchoice == 3:
        print("It's a Tie! Nobody wins.")

# Loss Section
    if computer == 1 and userchoice == 3:
        print("You Lose.")

    if computer == 3 and userchoice == 2:
        print("You Lose.")

    if computer == 2 and userchoice == 1:
        print("You Lose.")

# Win section
    if computer == 1 and userchoice == 2:
        print("You Win!")

    if computer == 2 and userchoice == 3:
        print("You Win!")

    if computer == 3 and userchoice == 1:
        print("You Win!")

# None Section
    if computer == 0 and userchoice == 1:
        print("The computer didn't pick anything... Sorry bout that...")

    if computer == 0 and userchoice == 2:
        print("The computer didn't pick anything... Sorry bout that...")

    if computer == 0 and userchoice == 3:
        print("The computer didn't pick anything... Sorry bout that...")

# While loop end        
    answer = input("Do you want to play again (y/n)? ")
    answer = answer.lower()[0]

                          

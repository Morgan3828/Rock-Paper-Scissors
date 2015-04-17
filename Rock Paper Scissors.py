# Rock, paper, Scissors
# By Morgan V.
# Set Values & Import

import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
answer = None

OPTIONS = ( None,
            "Rock",
            "Paper",
            "Scissors")

# Create a window
root = Tk()
w = Label(root, text="Rock, Paper, Scissors")
w.pack()

# While Loop

while answer != 2:    
    userchoice = simpledialog.askinteger("  1 for Rock, 2 for Paper, 3 for Scissors. ",
                                " Rock, Paper, or Scissors ? :"))
# Randomization AI
    computer = random.randrange(len(OPTIONS))
    messagebox.showinfo("The computer chose {}.".format( OPTIONS[computer]))
        
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
    else:
                
# While loop end        
    answer = simpledialog.askinteger("Do you want to play again (y/n)? ",
                                     "1 = Yes 2 = No")
    answer = answer.lower()[0]

                          

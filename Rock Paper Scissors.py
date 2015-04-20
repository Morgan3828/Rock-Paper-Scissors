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
    userchoice = simpledialog.askinteger(" Rock, Paper, or Scissors? :",
                                         "1 for Rock, 2 for Paper, 3 for Scissors")
# Randomization AI
    computer = random.randrange(len(OPTIONS))
    messagebox.showinfo("Rock, Paper, Scissors",
                        "The computer chose {}.".format( OPTIONS[computer]))
        
# Tie section
    if computer == 1 and userchoice == 1:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "It's a Tie! Nobody wins.")

    if computer == 2 and userchoice == 2:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "It's a Tie! Nobody wins.")

    if computer == 3 and userchoice == 3:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "It's a Tie! Nobody wins.")

# Loss Section
    if computer == 1 and userchoice == 3:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Lose.")

    if computer == 3 and userchoice == 2:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Lose.")

    if computer == 2 and userchoice == 1:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Lose.")

# Win section
    if computer == 1 and userchoice == 2:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Win!")

    if computer == 2 and userchoice == 3:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Win!")

    if computer == 3 and userchoice == 1:
        messagebox.showinfo("Rock, Paper, Scissors",
                            "You Win!")

# None Section
    if computer == None and userchoice == 1:		
        answer = 1		                
		
    if computer == None and userchoice == 2:		
        answer = 1		
		
    if computer == None and userchoice == 3:
        answer = 1
                
# While loop end        
    answer = simpledialog.askinteger("Do you want to play again (y/n)? ",
                                     "1 = Yes 2 = No")

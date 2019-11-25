from tkinter import *
import random
import tkinter
from tkinter import ttk
#Made by kai piper
#rps stands for rock paper scissors

#Global Variables Below
user = int
computer = int
win = 0
lose = 0

def rps(win, lose, user):
    computer = random.randrange(1,4)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
            
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)   
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        

top = tkinter.Tk()
#Sets windiw title
top.wm_title("Rock paper scissors by Kai Piper")
#Sets window size
top.geometry("335x200")
#Stops window for being resized
top.resizable(False, False)
#Button for Rock
photo1=PhotoImage(file="rock.gif")
B1 = ttk.Button(top, text ="Rock",image = photo1, command = lambda: rps(win, lose, 1))
B1.grid(row=0, column=1)
#Button for paper
photo2=PhotoImage(file="paper.gif")
B2 = ttk.Button(top, text ="Paper",image = photo2, command = lambda: rps(win, lose, 2))
B2.grid(row=0, column=2)
#Button for Scissors
photo3=PhotoImage(file="scissors.gif.")
B3 = ttk.Button(top, text ="Scissors",image = photo3, command = lambda: rps(win, lose, 3))
B3.grid(row=0, column=3)
space = tkinter.Label(top, text="")
space.grid(row=1)
var = StringVar()
var.set('Welcome!')
l = Label(top, textvariable = var)
l.grid(row=2, column=2)
wins = IntVar()
wins.set(win)
w = Label(top, textvariable = wins)
w.grid(row=4, column=2)
labeled = Label(top, text = "Score:")
labeled.grid(row=3, column=2)
copy = Label(top, text= "Rock paper scissors By Kai Piper")
copy.grid(row=5, column=2)
top.attributes("-topmost", True)
top.geometry("+300+300")
try:
    #If icon is found then it will display it
    top.iconbitmap('icon.ico')
except:
    pass
top.mainloop()

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
top.geometry("340x200")
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

popup1 = Menu(B1, tearoff=0)
popup1.add_command(label="Select Rock", command = lambda: rps(win, lose, 1)) 


def do_popup(event):
    # display the popup menu
    try:
        popup1.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup1.grab_release()
B1.bind("<Button-3>", do_popup)


popup2 = Menu(B2, tearoff=0)
popup2.add_command(label="Select Paper", command = lambda: rps(win, lose, 2)) 


def do_popup(event):
    # display the popup menu
    try:
        popup2.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup2.grab_release()
B2.bind("<Button-3>", do_popup)


popup3 = Menu(B3, tearoff=0)
popup3.add_command(label="Select Scissors", command = lambda: rps(win, lose, 3)) 


def do_popup(event):
    # display the popup menu
    try:
        popup3.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup3.grab_release()
B3.bind("<Button-3>", do_popup)


space = tkinter.Label(top, text="")
space.grid(row=1)
var = StringVar()
var.set('Welcome to RPS!')
l = Label(top, textvariable = var, font=("Helvetica", 8, "bold italic"))
l.grid(row=2, column=2)
wins = IntVar()
wins.set(win)
w = Label(top, textvariable = wins, font=("Helvetica", 8, "bold italic"))
w.grid(row=4, column=2)
labeled = Label(top, text = "Score:", font=("Helvetica", 8, "bold italic"))
labeled.grid(row=3, column=2)
copy = Label(top, text= "Rock paper scissors By Kai Piper", font=("Helvetica", 8, "bold italic"))
copy.grid(row=5, column=2)
top.attributes("-topmost", True)
top.geometry("+300+300")
try:
    #If icon is found then it will display it
    top.iconbitmap('icon.ico')
except:
    pass

top.config(cursor="dot") #this sets the custom cursor
top.bind('<Escape>', lambda e: top.destroy()) # this sets escape as a exit key

def About():
    window = Tk()
    window.title("RPS ABOUT PAGE")
    info = Label(window, text = "About", font=("Helvetica", 10, "bold italic"))
    info.pack()
    info = Label(window, text = """Version Number =  3.0
Developer = Kai Piper""", font=("Helvetica", 6, "bold italic"))
    info.pack()

    try:
        #If icon is found then it will display it
        window.iconbitmap('icon.ico')
    except:
        pass
    window.attributes("-topmost", True)
    window.resizable(False, False)
    window.mainloop()
def exit1():
    top.destroy()  
# create a menu
popup = Menu(top, tearoff=0)
popup.add_command(label="About", command = About) 
popup.add_separator()
popup.add_command(label="Exit", command = exit1)

def do_popup(event):
    # display the popup menu
    try:
        popup.tk_popup(event.x_root, event.y_root, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()
top.bind("<Button-3>", do_popup)
top.mainloop()

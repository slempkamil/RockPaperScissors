import random
from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Rock Paper Scissors')
Label(root, text='Rock Paper Scissors', font='arial 20 bold').pack()
Label(root, text='Choose one:', font='arial 15 bold').place(x=40, y=50)
Label(root, text='Player Choice:', font='arial 15 bold').place(x=40, y=130)
Label(root, text='Computer Choice:', font='arial 15 bold').place(x=200, y=130)


def rock():
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)

    if computer_action == "rock":
        match_result = "Draw!"
        comp_value = "Rock"
    elif computer_action == "paper":
        match_result = "Computer won!"
        comp_value = "Paper"
    elif computer_action == "scissors":
        match_result = "Player won!"
        comp_value = "Scissors"

    label.config(text=match_result)
    label_player.config(text="Rock")
    label_computer.config(text=comp_value)


def paper():
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)

    if computer_action == "rock":
        match_result = "Player won!"
        comp_value = "Rock"
    elif computer_action == "paper":
        match_result = "Draw!"
        comp_value = "Paper"
    elif computer_action == "scissors":
        match_result = "Computer won!"
        comp_value = "Scissors"

    label.config(text=match_result)
    label_player.config(text="Paper")
    label_computer.config(text=comp_value)


def scissors():
    actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(actions)

    if computer_action == "rock":
        match_result = "Computer won!"
        comp_value = "Rock"
    elif computer_action == "paper":
        match_result = "Player won!"
        comp_value = "Paper"
    elif computer_action == "scissors":
        match_result = "Draw!"
        comp_value = "Scissors"

    label.config(text=match_result)
    label_player.config(text="Scissors")
    label_computer.config(text=comp_value)


Button(root, text="Rock", font='arial 15', command=rock, bg='ghost white').place(x=60, y=90)
Button(root, text="Paper", font='arial 15', command=paper, bg='ghost white').place(x=130, y=90)
Button(root, text="Scissors", font='arial 15', command=scissors, bg='ghost white').place(x=210, y=90)
label = Label(text="", font=('Coveat', 25, 'bold'), bg="ghost white")
label.place(x=60, y=220)
label_player = Label(text="", font=('Coveat', 25, 'bold'), bg="ghost white")
label_player.place(x=40, y=160)
label_computer = Label(text="", font=('Coveat', 25, 'bold'), bg="ghost white")
label_computer.place(x=200, y=160)

root.mainloop()

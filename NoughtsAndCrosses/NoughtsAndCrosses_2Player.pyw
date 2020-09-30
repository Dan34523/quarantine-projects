from tkinter import *

# Setting up the window
root = Tk()
root['bg'] = 'black'
root.resizable(0, 0)


# Changes the status for a prescribed number of milliseconds
def change_status(new_status, time):
    global turn
    turnLabel.config(text=new_status)
    root.after(time, lambda: turnLabel.config(text="{}'s turn".format(turn)))


# Checks who's turn it is and passes the turn to the other player
def change_turn():
    global turn
    if turn == "O":
        turn = "X"
        turnLabel.config(text="{}'s turn".format(turn))
    elif turn == "X":
        turn = "O"
        turnLabel.config(text="{}'s turn".format(turn))


# Checks for 3 in a row
def check_win():
    # -------------------------------------- Horizontal wins -------------------------------------------
    if a1["text"] == a2["text"] == a3["text"] == "X" or a1["text"] == a2["text"] == a3["text"] == "O":
        win(a1)
        change_button_colours(a1, a2, a3, "light green")

    elif b1["text"] == b2["text"] == b3["text"] == "X" or b1["text"] == b2["text"] == b3["text"] == "O":
        win(b1)
        change_button_colours(b1, b2, b3, "light green")

    elif c1["text"] == c2["text"] == c3["text"] == "X" or c1["text"] == c2["text"] == c3["text"] == "O":
        win(c1)
        change_button_colours(c1, c2, c3, "light green")

    # --------------------------------------- Vertical wins ---------------------------------------------
    elif a1["text"] == b1["text"] == c1["text"] == "X" or a1["text"] == b1["text"] == c1["text"] == "O":
        win(a1)
        change_button_colours(a1, b1, c1, "light green")

    elif a2["text"] == b2["text"] == c2["text"] == "X" or a2["text"] == b2["text"] == c2["text"] == "O":
        win(a2)
        change_button_colours(a2, b2, c2, "light green")

    elif a3["text"] == b3["text"] == c3["text"] == "X" or a3["text"] == b3["text"] == c3["text"] == "O":
        win(a3)
        change_button_colours(a3, b3, c3, "light green")

    # ---------------------------------------- Diagonal wins ---------------------------------------------
    elif a1["text"] == b2["text"] == c3["text"] == "X" or a1["text"] == b2["text"] == c3["text"] == "O":
        win(a1)
        change_button_colours(a1, b2, c3, "light green")

    elif a3["text"] == b2["text"] == c1["text"] == "X" or a3["text"] == b2["text"] == c1["text"] == "O":
        win(a3)
        change_button_colours(a3, b2, c1, "light green")

    # If no one wins
    else:
        change_turn()

    if check_draw():
        root.after(5000, lambda: root.quit())


# Checks if all boxes are taken up
def check_draw():
    global boxes
    filled_boxes = 0
    for box in boxes:
        if box["text"] == "X" or box["text"] == "O":
            filled_boxes += 1
    if filled_boxes == 9:
        a1.config(command=lambda: None)
        a2.config(command=lambda: None)
        a3.config(command=lambda: None)

        b1.config(command=lambda: None)
        b2.config(command=lambda: None)
        b3.config(command=lambda: None)

        c1.config(command=lambda: None)
        c2.config(command=lambda: None)
        c3.config(command=lambda: None)

        turnLabel.config(text="It's a draw.")
        return True
    else:
        return False


def change_button_colours(button1, button2, button3, colour):
    button1.config(background=colour)
    button2.config(background=colour)
    button3.config(background=colour)


# Functions for each button
def a1():
    if a1["text"] == "X" or a1["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        a1.config(text=turn)
        check_win()


def a2():
    if a2["text"] == "X" or a2["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        a2.config(text=turn)
        check_win()


def a3():
    if a3["text"] == "X" or a3["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        a3.config(text=turn)
        check_win()


def b1():
    if b1["text"] == "X" or b1["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        b1.config(text=turn)
        check_win()


def b2():
    if b2["text"] == "X" or b2["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        b2.config(text=turn)
        check_win()


def b3():
    if b3["text"] == "X" or b3["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        b3.config(text=turn)
        check_win()


def c1():
    if c1["text"] == "X" or c1["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        c1.config(text=turn)
        check_win()


def c2():
    if c2["text"] == "X" or c2["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        c2.config(text=turn)
        check_win()


def c3():
    if c3["text"] == "X" or c3["text"] == "O":
        change_status("Already filled in", 2500)
    else:
        c3.config(text=turn)
        check_win()


# Removes the command from each button and tells the players who won
def win(cell):
    a1.config(command=lambda: None)
    a2.config(command=lambda: None)
    a3.config(command=lambda: None)

    b1.config(command=lambda: None)
    b2.config(command=lambda: None)
    b3.config(command=lambda: None)

    c1.config(command=lambda: None)
    c2.config(command=lambda: None)
    c3.config(command=lambda: None)

    turnLabel.config(text="{} has won!!".format(cell["text"]))
    root.after(5000, lambda: root.quit())


turn = "X"
turnLabel = Label(root, text="{}'s turn".format(turn), font="Helvetica 20 bold")

# All the buttons
a1 = Button(root, text="", font="Helvetica 20 bold", command=a1, height=4, width=10)
a2 = Button(root, text="", font="Helvetica 20 bold", command=a2, height=4, width=10)
a3 = Button(root, text="", font="Helvetica 20 bold", command=a3, height=4, width=10)

b1 = Button(root, text="", font="Helvetica 20 bold", command=b1, height=4, width=10)
b2 = Button(root, text="", font="Helvetica 20 bold", command=b2, height=4, width=10)
b3 = Button(root, text="", font="Helvetica 20 bold", command=b3, height=4, width=10)

c1 = Button(root, text="", font="Helvetica 20 bold", command=c1, height=4, width=10)
c2 = Button(root, text="", font="Helvetica 20 bold", command=c2, height=4, width=10)
c3 = Button(root, text="", font="Helvetica 20 bold", command=c3, height=4, width=10)

# List to check through in check_draw() function
boxes = [a1, a2, a3, b1, b2, b3, c1, c2, c3]

a1.grid(row=0, column=0, padx=1, pady=1)
a2.grid(row=0, column=1, padx=1, pady=1)
a3.grid(row=0, column=2, padx=1, pady=1)

b1.grid(row=1, column=0, padx=1, pady=1)
b2.grid(row=1, column=1, padx=1, pady=1)
b3.grid(row=1, column=2, padx=1, pady=1)

c1.grid(row=2, column=0, padx=1, pady=1)
c2.grid(row=2, column=1, padx=1, pady=1)
c3.grid(row=2, column=2, padx=1, pady=1)

# Tells the users whose turn it is but also tells the player if the box is already filled in at times
turnLabel.grid(row=3, columnspan=3, sticky=N + E + S + W)

# Starts the program
if __name__ == "__main__":
    root.mainloop()

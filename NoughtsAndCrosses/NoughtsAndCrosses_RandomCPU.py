from tkinter import *
import random

root = Tk()
statusBar = Label(root, text="Click to place your X", font="bold 17")
board = None

'''
In this version, the player chooses a slot and the computer then chooses a random slot
'''


class Board:
    def __init__(self):
        self.boxes = []
        for i in range(9):
            new_box = Box(root, i // 3, i % 3, self)
            self.boxes.append(new_box)

    def all_boxes_full(self):
        for box in self.boxes:
            if box.available:
                return False
        return True

    def available_boxes(self):
        available_box_list = []
        for box in self.boxes:
            if box.available:
                available_box_list.append(box)
        return available_box_list

    def get_random_available_box(self):
        return random.choice(self.available_boxes())

    def check_win(self):
        # Horizontal Combinations
        if self.boxes[0].text == self.boxes[1].text == self.boxes[2].text and not self.boxes[0].available:
            self.on_win(self.boxes[0].text)
            return True

        elif self.boxes[3].text == self.boxes[4].text == self.boxes[5].text and not self.boxes[3].available:
            self.on_win(self.boxes[3].text)
            return True

        elif self.boxes[6].text == self.boxes[7].text == self.boxes[8].text and not self.boxes[6].available:
            self.on_win(self.boxes[6].text)
            return True

        # Vertical Combinations
        elif self.boxes[0].text == self.boxes[3].text == self.boxes[6].text and not self.boxes[0].available:
            self.on_win(self.boxes[0].text)
            return True

        elif self.boxes[1].text == self.boxes[4].text == self.boxes[7].text and not self.boxes[1].available:
            self.on_win(self.boxes[1].text)
            return True

        elif self.boxes[2].text == self.boxes[5].text == self.boxes[8].text and not self.boxes[2].available:
            self.on_win(self.boxes[2].text)
            return True

        # Diagonal Combinations
        elif self.boxes[0].text == self.boxes[4].text == self.boxes[8].text and not self.boxes[0].available:
            self.on_win(self.boxes[0].text)
            return True

        elif self.boxes[2].text == self.boxes[4].text == self.boxes[6].text and not self.boxes[2].available:
            self.on_win(self.boxes[2].text)
            return True

        else:
            return False

    def on_win(self, winner):
        for box in self.boxes:
            box.button.config(command=lambda: None)

        send_status_message((winner + " wins!"), 1, False)
        root.after(3000, restart_board)


class Box:
    def __init__(self, master: Tk, this_row: int, this_column: int, parent_board: Board):
        self.parent = parent_board
        self.masterWindow: Tk = master
        self.row = this_row
        self.column = this_column
        self.location = str(this_column) + ", " + str(this_row)
        self.available: bool = True
        self.text = ""
        self.button: Button = Button(master, text=self.text, height=4, width=9, font="Helvetica 20 bold", command=self.player_turn)

    def player_turn(self):
        if self.available:
            self.set_button_text("X")
            if self.parent.check_win():
                return
            computer_turn(self.parent)
            self.parent.check_win()

    def set_button_text(self, new_text: str):
        if self.available:
            self.button.config(text=new_text)
            self.text = new_text
            self.available = False

        else:
            send_status_message("Not Available", 1500, True)


def computer_turn(game_board: Board):
    if game_board.all_boxes_full():
        send_status_message("Draw", 1, False)
        return
    else:
        random_box: Box = game_board.get_random_available_box()
        random_box.set_button_text("O")


def send_status_message(msg: str, length: int, temporary: bool):
    old_msg = statusBar.cget("text")
    statusBar.config(text=msg)

    if temporary:
        root.after(length, lambda: statusBar.config(text=old_msg))


def initialise_board():
    global board
    board = Board()
    for box in board.boxes:
        box.button.grid(row=box.row, column=box.column)
    statusBar.config(text="Click to place your X")
    statusBar.grid(row=3, columnspan=3, sticky=N + S + E + W)


def restart_board():
    global board
    statusBar.grid_forget()
    for box in board.boxes:
        box.button.grid_forget()
    board = None

    initialise_board()


initialise_board()
root.mainloop()

"""
In this version, the player chooses a slot and the computer then chooses the best available slot based
on the Mini-max Algorithm. Uses a recursive post-order graph traversal to find the optimal move to take

In this implementation, the user is known as the maximising player, and the computer is known as the minimising
player
"""

from tkinter import *
import random

root = Tk()
root.resizable(0, 0)
root["bg"] = "black"
statusBar = Label(root, text="Click to claim box", font="bold 17")


class Board:
    # Creates a new board with nine boxes. Adds the boxes to a list
    def __init__(self):
        self.boxes = []
        for i in range(9):
            new_box = Box(root, i // 3, i % 3, self, i)
            self.boxes.append(new_box)

    # Returns whether every single box is full or not, used to see if there is a draw
    def all_boxes_full(self):
        for box in self.boxes:
            if box.available:
                return False
        return True

    # Returns a list off all empty boxes
    def available_boxes(self):
        available_box_list = []
        for box in self.boxes:
            if box.available:
                available_box_list.append(box)
        return available_box_list

    def get_random_available_box(self):
        return random.choice(self.available_boxes())

    # Checks all the win combinations and returns whether there is a winner and who the winner is
    def check_win(self):
        # Horizontal Combinations
        if self.boxes[0].text == self.boxes[1].text == self.boxes[2].text and not self.boxes[0].available:
            return True, self.boxes[0].text

        elif self.boxes[3].text == self.boxes[4].text == self.boxes[5].text and not self.boxes[3].available:
            return True, self.boxes[3].text

        elif self.boxes[6].text == self.boxes[7].text == self.boxes[8].text and not self.boxes[6].available:
            return True, self.boxes[6].text

        # Vertical Combinations
        elif self.boxes[0].text == self.boxes[3].text == self.boxes[6].text and not self.boxes[0].available:
            return True, self.boxes[0].text

        elif self.boxes[1].text == self.boxes[4].text == self.boxes[7].text and not self.boxes[1].available:
            return True, self.boxes[1].text

        elif self.boxes[2].text == self.boxes[5].text == self.boxes[8].text and not self.boxes[2].available:
            return True, self.boxes[2].text

        # Diagonal Combinations
        elif self.boxes[0].text == self.boxes[4].text == self.boxes[8].text and not self.boxes[0].available:
            return True, self.boxes[0].text

        elif self.boxes[2].text == self.boxes[4].text == self.boxes[6].text and not self.boxes[2].available:
            return True, self.boxes[2].text

        else:
            return False, None

    # Changes the buttons to stop clicks adding symbols after the game has ended. Sets the status bar to show the winner
    def on_win(self, winner):
        for box in self.boxes:
            box.button.config(command=lambda: None)

        send_status_message((winner + " wins!"), 1, False)

    # Returns whether the game has been won and calls the Board.on_win() function
    def win(self):
        result = self.check_win()
        if result[0]:
            self.on_win(result[1])

        return result[0]

    # Used to find the score of the current board based on who won this board.
    def get_static_evaluation(self):
        result = self.check_win()
        if result[0]:
            if result[1] == "X":
                return 1
            else:
                return -1
        elif self.all_boxes_full():
            return 0
        else:
            return None


class Box:
    def __init__(self, master: Tk, this_row: int, this_column: int, parent_board: Board, index: int):
        self.parent = parent_board
        self.masterWindow: Tk = master
        self.row = this_row
        self.column = this_column
        self.index = index
        self.available = True
        self.text = ""
        self.button = Button(master, text=self.text, height=4, width=9, font="Helvetica 20 bold", command=self.player_turn)

    # Called when the user presses the button. Places the mark and checks for a win. Places the computers the mark and checks again
    def player_turn(self):
        if self.available:
            self.set_button_text("X", False, True)
            if self.parent.win():
                return
            computer_turn(self.parent, None)
            if self.parent.win():
                return
            elif self.parent.all_boxes_full():
                send_status_message("Tie!", 1, False)

    # Function to configure the button after it has been pressed. Checks to see if the box is available or I specified
    # it to change regardless. Also contains an override to skip setting the text visible to the user, used in the
    # mini-max algorithm to save time
    def set_button_text(self, new_text: str, force_change: bool, update_button: bool):
        if self.available or force_change:
            self.text = new_text
            self.available = False
            if update_button:
                self.button.config(text=new_text)

        else:
            send_status_message("Not Available", 1500, True)


def computer_turn(game_board: Board, manual_index):
    # If I specified the index to place computer mark. Skips the mini-max algorithm
    if manual_index is not None:
        game_board.boxes[manual_index].set_button_text("O", False, True)
        return

    else:
        # Computer is minimising so I set the first best score to a very large positive number
        best_score = 100000
        best_move = 0

        # Used to place the mark in the middle if it is the computer's first turn (minimax leads to this anyways
        # no matter where user places mark). Optimises as minimax is O(n!) so skipping 8 iterations saves a lot
        # of time
        if len(game_board.available_boxes()) == 8 and game_board.boxes[4].available:
            game_board.boxes[4].set_button_text("O", False, True)
            return

        # Calls the minimax algorithm for the first time
        for box in game_board.boxes:
            if box.available:
                box.set_button_text("O", False, False)
                score = minimax(game_board, 0, True)
                box.set_button_text("", True, False)
                box.available = True
                if score < best_score:
                    best_score = score
                    best_move = box.index
        game_board.boxes[best_move].set_button_text("O", False, True)


def minimax(game_board: Board, depth: int, is_maximising: bool):
    result = game_board.get_static_evaluation()

    # If the board is an end state i.e. the game has finished
    if result is not None:
        return result

    # If maximising, the best move is the most positive, the next layer down would be minimising
    if is_maximising:
        best_score = -10000
        for box in game_board.boxes:
            if box.available:
                box.set_button_text("X", False, False)
                score = minimax(game_board, depth + 1, False)  # Sets the next layer to minimising
                box.set_button_text("", True, False)
                box.available = True
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = 10000
        for box in game_board.boxes:
            if box.available:
                box.set_button_text("O", False, False)
                score = minimax(game_board, depth + 1, True)  # Sets the next layer to maximising
                box.set_button_text("", True, False)
                box.available = True
                best_score = min(best_score, score)
        return best_score


# Used to temporarily set the text of the status bar to a given parameter
def send_status_message(msg: str, length: int, temporary: bool):
    old_msg = statusBar.cget("text")
    statusBar.config(text=msg)

    if temporary:
        root.after(length, lambda: statusBar.config(text=old_msg))


# Creates a new board and places all boxes into the window
board = Board()
for each_box in board.boxes:
    each_box.button.grid(row=each_box.row, column=each_box.column, padx=1, pady=1)
statusBar.grid(row=3, columnspan=3, sticky=N + S + E + W)

# Chooses whether computer goes first or the player
random_int = random.randint(1, 3)
if random_int == 2:
    computer_turn(board, random.choice([0, 2, 4, 6, 8]))

root.mainloop()

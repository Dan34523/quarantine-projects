import random
from tkinter import *

# Root is the parent window. Any changes to the window happens through this variable
root = Tk()
root.resizable(0, 0)  # User can't resize the window
root.configure(background="white")

stage = 0
stages = ["Stage 0.png",
          "Stage 1.png",
          "Stage 2.png",
          "Stage 3.png",
          "Stage 4.png",
          "Stage 5.png",
          "Stage 6.png",
          "Stage 7.png",
          "Stage 8.png"]


def generate_word(file):
    # Opens the file with the possible words and splits the long string into individual words
    with open(file, "r") as f:
        lines = f.read().splitlines()

    # Returns a random word from the list
    return random.choice(lines)


# The word the user has guessed
actual_word = generate_word("Original Dictionary.txt")

# The sequence of dashes and letters that the user can see
word_on_screen = ""

# List of guesses from the user. Used to check if the guess is repeated
already_guessed = []
already_guessed_text = "Letters inputted:\n  "


# Changes the title text for 2 seconds. Used for sending status updates to the user.
# root.after() is used to delay a piece of code from being executed
# Lambdas are used as root.after() takes a function for the second argument.
def update_title(new_text, old_text):
    title.config(text=new_text)
    root.after(2000, lambda: title.config(text=old_text))


# Function that is called when user presses the submit button
def guess_a_letter():
    global stage
    guess = letter_entry.get()

    # Following selection block checks to see whether guess is valid and correct

    # If user has already inputted the guess
    if guess in already_guessed:
        update_title("Already Inputted!", "Hangman!")

    # If the guess isn't a single letter
    elif len(guess) != 1:
        update_title("Guess is invalid!", "Hangman")

    # If the guess is correct
    elif guess in actual_word:
        already_guessed.append(guess)

    # If the guess is incorrect
    else:
        stage += 1
        already_guessed.append(guess)

    # As the program checks if the guess is correct before changing stage, it eliminates the need to see if the guess is
    # a letter or if it is a number, symbol etc.

    # Clears the text entry widget. All widgets can be seen from line 99
    letter_entry.delete(0, END)
    update_widgets()


# Function used when the user presses the enter key instead of the submit button
def guess_a_letter_key_press(event):
    guess_a_letter()


def on_win():
    root.configure(background="light blue")
    title.config(text="You won!", background="light blue")
    word_on_screen_label.config(background="light blue")
    already_guessed_label.config(background="light blue")
    root.after(0, lambda: root.config(stage_label.config(image=win_picture1, background="light blue")))
    root.after(750, lambda: root.config(stage_label.config(image=win_picture2)))


# When the user presses the enter key, it submits a guess
root.bind("<Return>", guess_a_letter_key_press)

# Tkinter variables and widgets:

# Picture used to show progression of hanging man
stage_picture = PhotoImage(file=stages[stage])

# 2 frames that make the man look like he is waving
win_picture1 = PhotoImage(file="Win 1.png")
win_picture2 = PhotoImage(file="Win 2.png")

# Widget that holds the image of the man
stage_label = Label(root, image=stage_picture, background="white")

# Text entry box used to enter guesses with the button used to submit them
letter_entry = Entry(background="#f2f2f2", width=12, font="Helvetica 14")
letter_submit = Button(root, text="Submit", command=guess_a_letter, width=18, font="Helvetica 12")

# Title label
title = Label(root, text="Welcome to Hangman!", font="Helvetica 24 bold", background="white", width=35)

# Label showing guesses the user has submitted
already_guessed_label = Label(root, text=already_guessed_text, font="Helvetica 16 bold", background="white")

# Label showing the sequence of dashes and letters that the user has guessed
word_on_screen_label = Label(root, text=word_on_screen, font="Helvetica 20 bold", background="white")


def update_widgets():
    global word_on_screen, already_guessed_text, stage_picture

    # Checks to see if the user has lost, removes the guess entry widgets so additional guesses can't be made
    if stage >= 8:
        letter_entry.grid_forget()
        letter_submit.grid_forget()
        title.config(text="You lost! The word was {}".format(actual_word))

    # Running count that keeps track of how many letters have been correctly guessed
    count = 0
    word_on_screen = ""
    already_guessed_text = "Letters inputted:\n  "

    # For loop that goes through the actual word.
    # If the letter has been guessed, it adds the letter, otherwise it adds a dash
    for letter in actual_word:
        if letter not in already_guessed:
            word_on_screen = "{}{}".format(word_on_screen, " _ ")
        else:
            word_on_screen = "{}{}".format(word_on_screen, letter)
            count += 1

    # Submits the new word to the label
    word_on_screen_label.configure(text=word_on_screen)

    # Checks to see if all letters have been guessed. Removes letter entry and plays the win animation
    if count == len(actual_word):
        letter_entry.grid_forget()
        letter_submit.grid_forget()
        on_win()

    # Adds all the guessed letters to a nicely formatting string
    for letter in already_guessed:
        already_guessed_text = "{}{}, ".format(already_guessed_text, letter)

    # Removes the comma and space at the end of the string
    already_guessed_text = already_guessed_text[:-2]
    already_guessed_label.config(text=already_guessed_text)

    # Sets the picture to the current stage
    stage_picture = PhotoImage(file=stages[stage])
    stage_label.config(image=stage_picture)


update_widgets()

# Places the widgets in the correct place on the GUI
title.grid(columnspan=3, padx=25)
stage_label.grid(column=2, columnspan=2, rowspan=3)
word_on_screen_label.grid(column=0, row=1, columnspan=2)
letter_entry.grid(column=0, row=2)
letter_submit.grid(column=1, row=2)
already_guessed_label.grid(columnspan=2, row=3)

root.mainloop()

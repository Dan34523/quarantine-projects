import random
import time
import sys

# Responses of the original 8 Ball taken from Wikipedia
responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
             "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
             "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
             "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful"
        ]


def intro():
    print("Hello. What is your name?")
    myName = input("> ")

    # Use string formatting to add name to greeting
    print("Well, hello %s. Let's play a game. You ask a question and I will try my best to answer it." % myName)


def userinput():
    question = 'Enter your question:'
    print(question)
    input("> ") # Reply is random, no need to store the question

    print("\nThinking..\n")
    time.sleep(3)
    print(random.choice(responses))

    final()


def final():
    print("Would you like to ask another question?")
    user_reply = input('> ')
    while (input):
        if user_reply.lower() == "yes":
            userinput()

        else:
            print("\nThanks for playing!\n")
            time.sleep(1)
            sys.exit(0)


intro()
userinput()

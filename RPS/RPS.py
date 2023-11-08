import time
from random import randint

def RockPaperScissors():
    # This creates a list of options for the player and computer
    t = ["rock", "paper", "scissors"]

    # This assigns a random option to the computer
    computer = t[randint(0, 2)]

    while True:
        # Get the player's choice
        player = input("Write Rock, Paper, or Scissors?").lower()

        if player not in t:
            print("That's not a valid play. Check your spelling!")
            continue

        print("Computer chose:", computer)

        if player == computer:
            print("Tie!")

        elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
            print("You win!", player, "beats", computer)

        else:
            print("You lose!", computer, "beats", player)

        replay = input("Do you want to play again? (yes/no): ").lower()

        if replay in ['yes', 'y']:
            computer = t[randint(0, 2)]
            continue

        elif replay in ['no', 'n']:
            print("Okay, it was fun to play with you!")
            print("Please come again.")
            break

        else:
            print("I apologize, I did not catch that. Please repeat.")

RockPaperScissors()

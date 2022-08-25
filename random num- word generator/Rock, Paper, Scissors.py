from random import randint

#This creates a list of options for the player and computer

t = ["Rock", "Paper", "Scissors"]

#This assigns a random option to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:

#set player to True
    player = input("Rock, Paper, Scissors?")

    if player == computer:
        print("Tie!")
        print("Do you want to play again?")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print("Do you want to play again?")
        else:
            print("You win!", player, "smashes", computer)
            print("Do you want to play again?")

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print("Do you want to play again?")
        else:
            print("You win!", player, "covers", computer)
            print("Do you want to play again?")

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print("Do you want to play again?")
        else:
            print("You win!", player, "cut", computer)
            print("Do you want to play again?")
    else:
        print("That's not a valid play. Check your spelling!")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
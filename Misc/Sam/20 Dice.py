import random
from Misc.Sam import time

# Enter the minimum and maximum limits of the dice rolls below

min_val = 1

max_val = 20


# the variable that stores the user’s decision

def roll():
    roll_dice = input("Do you wish to role the dice?: ").lower()

    # The dice roll loop if the user wants to continue
    if roll_dice == "yes" or roll_dice == "y":
        print("Dices rolling...")
        time.sleep(2.5)
        print("The value is:")
        time.sleep(2)

        # Printing the randomly generated variable of the first dice
        print(random.randint(min_val, max_val))

    elif roll_dice == "no" or roll_dice != "n":
        print("Thanks for playing")
        exit()

    elif roll_dice != "yes" or roll_dice != "y":
        print("That is not a correct value")
        roll()

    # Here the user enters yes or y to continue and any other input ends the program
    roll_dice = input("Roll the dice again?: ").lower()

    if roll_dice == "yes" or roll_dice == "y":
        print("Dices rolling...")
        time.sleep(2.5)
        print("The value is:")
        time.sleep(2)

        # Printing the randomly generated variable of the dice
        print(random.randint(min_val, max_val))

    elif roll_dice == "no" or roll_dice != "n":
        print("Thanks for playing")
        exit()

    elif roll_dice == "yes" or roll_dice != "y":
        print("That is not a correct value")
        roll()

roll()
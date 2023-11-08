import random
import time

# Set the minimum and maximum values for the dice
min_val = 1
max_val = 20

# Function for rolling the dice
def roll():
    while True:
        roll_dice = input("Do you wish to roll the dice? (yes/no): ").lower()

        if roll_dice in ['yes', 'y']:
            print("Dice rolling...")
            time.sleep(2.5)
            print("The value is:")
            time.sleep(2)
            print(random.randint(min_val, max_val))

            roll_again = input("Roll the dice again? (yes/no): ").lower()
            if roll_again in ['no', 'n']:
                print("Thanks for playing")
                break
            elif roll_again not in ['yes', 'y']:
                print("That is not a correct value.")
                continue

        elif roll_dice in ['no', 'n']:
            print("Thanks for playing")
            break

        else:
            print("That is not a correct value.")
            continue

roll()

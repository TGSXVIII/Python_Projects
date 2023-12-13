import random
from Misc.Sam import time


def coinToss():
    toss = input("Do you want to flip the coin again?: ").lower()

    if toss == "yes" or toss == "y":

        print("Coin is flipping...")
        time.sleep(1.5)
        print("It is...")
        time.sleep(1)

    elif toss == "no" or toss == "n":

        print("Thanks for playing")
        exit()

    elif toss != "yes" or toss != "y":

        print("That is not a correct value")
        coinToss()

    recordList = []
    heads = 0
    tails = 1
    onTheSide = 2
    flip = random.randint(0, 2)

    if (flip == 0):
        time.sleep(1)
        print("Heads")
        recordList.append("Heads")
    elif (flip == 1):
        time.sleep(1)
        print("Tails")
        recordList.append("Tails")
    elif (flip == 2):
        time.sleep(1)
        print("It landed on the side")
        recordList.append("onTheSide")

    def coinTossAgain ():
        toss = input("Do you want to flip the coin again?: ").lower()

        if toss == "yes" or toss == "y":

            print("Coin is flipping...")
            time.sleep(1.5)
            print("It is...")
            time.sleep(1)

        elif toss == "no" or toss == "n":

            print("Thanks for playing")
            exit()

        elif toss != "yes" or toss != "y":

            print("That is not a correct value")
            coinTossAgain()

        recordList = []
        heads = 0
        tails = 1
        onTheSide = 2
        flip = random.randint(0, 2)

        if (flip == 0):
            time.sleep(1)
            print("Heads")
            recordList.append("Heads")
        elif (flip == 1):
            time.sleep(1)
            print("Tails")
            recordList.append("Tails")
        elif (flip == 2):
            time.sleep(1)
            print("It landed on the side")
            recordList.append("onTheSide")

    coinTossAgain()

coinToss()

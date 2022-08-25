from random import randrange

import string

# This is what opens our txt file and gives us our word list
word_list = open("WordleWords.txt", "r")
words = word_list.read()

# The word we have to guess is set into a list
def convertAnswer(string):
    answer = list(string.split("\n"))
    return answer


words = convertAnswer(words)

# This chooses a random word in the list
randomOrd = words[randrange(0, len(words))]

# This adds a letter to the list to compare
ls = []
for character in randomOrd:
    ls.append(character)

print("Please write your name:")
username = input()
print(f"Hello {username}! Welcome to Wordle!")

rules = "Here are the rules" + "\n" + "1. You have to decide how many lives you want by typing a number from 1 to 10" + "\n" + "2. You have to write a 5 letter word" + "\n"

print(rules)
# This is where the player decides how many lives they want
print("How many lives do you want?")

while True:
    try:
        liv = int(input())
        break
    except ValueError:
        print("You have to write a number")

# This is where the game really begins
print(randomOrd)

print(f"Welcome {username} to Wordle")
print("Now you have to write a 5 letter word")


def wordle():
    global liv
    gæt = input().lower()

    if len(gæt) != 5:
        print("You have to write a 5 letter word")
        wordle()

    for character in gæt:
        if character not in string.ascii_letters:
            print("You have to use letters")
            wordle()

    gætls = []

    for character in gæt:
        gætls.append(character)
    for i in range(0, 5):
        if ls[i] == gætls[i]:
            print('🟩 ', end="")
        elif gætls[i] not in ls:
            print(end="🟥 ")
        elif gætls[i] in ls:
            print('🟨 ', end='')
    print(" ")

    if gæt == randomOrd:
        print("You win, Congratulations!")
        exit()

    elif gæt != randomOrd:
        liv -= 1
        print("Wrong, try again")
        print(f"You have {liv} lives left")

    if liv > 0:
        wordle()
    if liv == 0:
        exit()


wordle()


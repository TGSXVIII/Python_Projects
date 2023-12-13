from random import choice
import string

# This is what opens our txt file and gives us our word list
with open("WordleWords.txt", "r") as word_list:
    words = [word.strip() for word in word_list]

# This chooses a random word in the list
random_word = choice(words)

# This is where the player decides how many lives they want
print("Please write your name:")
username = input()
print(f"Hello {username}! Welcome to Wordle!")
rules = "Here are the rules\n1. You have to decide how many lives you want by typing a number from 1 to 10\n2. You have to write a 5 letter word\n"
print(rules)

while True:
    try:
        liv = int(input("How many lives do you want?\n"))
        if 1 <= liv <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("You have to write a number")

print(f"Welcome {username} to Wordle. Now you have to write a 5-letter word.")


def wordle():
    global liv, random_word
    guess = input().lower()

    if len(guess) != 5 or not all(char in string.ascii_lowercase for char in guess):
        print("You have to write a 5-letter word using only letters")
        wordle()

    for i, char in enumerate(guess):
        if char == random_word[i]:
            print('🟩 ', end="")
        elif char in random_word:
            print('🟨 ', end='')
        else:
            print('🟥 ', end='')

    print(" ")

    if guess == random_word:
        print("You win, Congratulations!")
        exit()
    else:
        liv -= 1
        if liv > 0:
            print("Wrong, try again")
            print(f"You have {liv} lives left")
            wordle()
        else:
            print("Game over. The word was:", random_word)
            exit()


if __name__ == '__main__':
    wordle()

from random import randrange

import string

# This is what opens our txt file and gives us our word list
P&I = open("Phrases & Idioms.txt", "r")

P&I = word_list.read()

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
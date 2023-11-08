import randfacts
import string
import time

fact = randfacts.get_fact()

def funFact():
    print("Here is your fact")
    time.sleep(1.5)
    print(fact)
    time.sleep(1)

    factReply = input("Would you like to hear another fact? ")

    # The jokes loop if the user wants to continue
    if factReply == "yes" or factReply == "y":
        print("Here is your joke")
        time.sleep(2.5)
        print(fact)
        time.sleep(2)

    elif factReply != string.ascii_letters:
        print("That is not a correct value")
        funFact()

    elif factReply == "no" or factReply != "n":
        print("Okay have a good day")
        exit()

funFact()

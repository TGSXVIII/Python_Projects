import string
import pyjokes
from Misc.Sam import time

Sams_joke = pyjokes.get_joke(language="en", category="all")


def jokes():
    print("Here is your joke")
    time.sleep(2.5)

    print(Sams_joke)
    time.sleep(2)

    jokes_reply = input("Would you like to hear another joke? ")

    # The jokes loop if the user wants to continue
    if jokes_reply == "yes" or jokes_reply == "y":
        print("Here is your joke")
        time.sleep(2.5)

        print(Sams_joke)
        time.sleep(2)

    elif jokes_reply != string.ascii_letters:
        print("That is not a correct value")
        jokes()

    elif jokes_reply == "no" or jokes_reply != "n":
        print("Okay have a good day")
        exit()

jokes()

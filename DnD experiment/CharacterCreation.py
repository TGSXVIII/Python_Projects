import time

def CharacterCreation():

    #Lets you write your name
    time.sleep(1)
    name = input("Well hello traveler what is your name?")

    #Checks if there are any numbers in name
    if any(chr.isdigit() for chr in name):
        print("That is not a valid name please try again")
        CharacterCreation()

    else:
        #Lets you decide your gender (depending on what gender you are you can romance specific people)
        time.sleep(1)
        gender = input("What gender are you? (male/female/other)")

    # Checks if there are any numbers in gender
    if any(chr.isdigit() for chr in gender):
        print("That is not a valid name please try again")
        CharacterCreation()

    else:
        # Depending on what sexuality you have you can romance specific people
        time.sleep(1)
        sexuality = input("What is your sexual orientation (hetro/bi/gay/pan/other)")

    # Checks if there are any numbers in sexuality
    if any(chr.isdigit() for chr in sexuality):
        print("That is not a valid input please try again")
        CharacterCreation()

    time.sleep(1)
    print(f"Well hell there {name}")

CharacterCreation()
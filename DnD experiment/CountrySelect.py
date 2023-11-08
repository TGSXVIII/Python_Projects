from CitySelect import citySelect
from CharacterCreation import *


#--- World select ---#
def countrySelect():

        countrySelectNumber = ("1", "2", "3", "4", "5", "6")
        countrySelectName = ("witdeaory", "drafroory", "warsorach", "trolosdom", "witdeaxus", "gimbadur")

        #This lets you decide which country you would like to start from
        time.sleep(1)
        print("Here are the different starting countries you can choose from")

        time.sleep(2)
        print("1. Witdeaory, The Ancient Territory of the elves")
        print("2. Drafroory, Territory of the Dragons")
        print("3. Warsorach, Reach of the Warriors")
        print("4. Trolosdom, The Kingdom of the Trolls")
        print("5. Witdeaxus, Nexus of the Witches")

        time.sleep(4)
        answer = input("Which country would you like to start your story from?").lower()


        if answer != countrySelectName or answer != countrySelectNumber:
            print("That is not a valid input please try again")
            citySelect()

        else:
            print("Thats not a valid input please try again")
            citySelect()

    countrySelect()
from CountrySelect import *
from CharacterCreation import *

# --- City select ---#
def citySelect():

    citySelectNumber1 = ("1", "2", "3", "4", "5", "6")
    citySelectName1 = ("")

    citySelectNumber2 = ("1", "2", "3", "4", "5", "6")
    citySelectName2 = ("")

    citySelectNumber3 = ("1", "2", "3", "4", "5", "6")
    citySelectName3 = ("")

    citySelectNumber4 = ("1", "2", "3", "4", "5", "6")
    citySelectName4 = ("")

    citySelectNumber5 = ("1", "2", "3", "4", "5", "6")
    citySelectName5 = ("")

    citySelectNumber6 = ("1", "2", "3", "4", "5", "6")
    citySelectName6 = ("")

    # --- Witdeaory ---#
    answer = input("Which city do you want to start in?")

    if answer == "1" or answer == "witdeaory":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Witdeaory, The Ancient Territory")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect1():
            time.sleep(1)
            print("1.")
            print("2.")
            print("3.")
            print("4.")

    # --- Drafroory ---#
    elif answer == "2" or answer == "drafroory":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Drafroory, Territory of the Dragons")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect2():
            time.sleep(1)
            print("1.")
            print("2.")
            print("3.")
            print("4.")

    # --- Warsorach ---#
    elif answer == "3" or answer == "warsorach":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Warsorach, Reach of the Warriors")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect3():
            time.sleep(1)
            print("1.")
            print("2.")
            print("3.")
            print("4.")

        # --- Trolosdom ---#
    elif answer == "4" or answer == "trolosdom":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Trolosdom The Kingdom of the Trolls")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect4():
            time.sleep(1)
            print("1.")
            print("2.")
            print("3.")
            print("4.")

            # ----------------------------------------------------------------------

            # --- Witdeaxus ---#
    elif answer == "5" or answer == "witdeaxus":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Witdeaxus, Nexus of the Witches")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect5():
            time.sleep(1)
            print("1.")
            print("2.")
            print("3.")
            print("4.")

        # ----------------------------------------------------------------------

        # --- Gimbadur ---#
    elif answer == "6" or answer == "gimbadur":
        time.sleep(1)
        print(f"Hello {CharacterCreation.name} welcome to the world of ...")
        print("Gimbadur, Sanctuary of the dwarves")

        time.sleep(1)
        answer = input("Which city do you want to start in?").lower()

        def citySelect6():
            time.sleep(1)
            print("1. Golgow, The Golden City")
            print("2. Deeyoto, The Deep City")
            print("3. Bronich, The Broken City")
            print("4. Hazpool, The Hazy City")

    citySelect6()
    citySelect5()
    citySelect4()
    citySelect3()
    citySelect2()
    citySelect1()
citySelect()
from CharacterCreation import *
import time

# Create a dictionary to map country numbers to their corresponding names
country_data = {
    "1": "Witdeaory, The Ancient Territory of the elves",
    "2": "Drafroory, Territory of the Dragons",
    "3": "Warsorach, Reach of the Warriors",
    "4": "Trolosdom, The Kingdom of the Trolls",
    "5": "Witdeaxus, Nexus of the Witches",
}

# Function to select a country
def countrySelect():

    time.sleep(1)
    print("Here are the different starting countries you can choose from:")

    time.sleep(2)
    for number, country in country_data.items():
        print(f"{number}. {country}")

    time.sleep(2)
    while True:
        answer = input("Which country would you like to start your story from? ").strip()

        if answer in country_data:
            countrySelected = country_data[answer]
            print(f"You have chosen {countrySelected}. Is this correct?")

            while True:
                check = input("Are you sure? (Yes/No): ").strip().lower()

                if check in ["yes", "y"]:
                    print(f"Well then, traveler, welcome to the country {countrySelected}.")
                    return
                elif check in ["no", "n"]:
                    print("Please select another country.")
                    break
                else:
                    print("That is an invalid input. Try again.")
        else:
            print("That is not a valid input. Please try again.")

# Start the country selection process
countrySelect()

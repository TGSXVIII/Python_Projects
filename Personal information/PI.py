def introduction():

    # User
    user = input("Hello, I am Sam, What is your name?: ")

    print(f"Your name is {user} is that correct?")

    reply = input().upper()

    if reply == 'Y' or "YES":
        print(f"Hello {user}")
        PersonalInformation()

    elif reply == 'N' or "NO":
        introduction()

    else:
        print('I apologies, I did not catch that. Please repeat.')
        introduction()

def PersonalInformation():

    # Birthday
    bDay = input("When is your birthday?: ")

    print(f"Your birthday is {bDay} is that correct?")

    reply = input().upper()

    if reply == 'Y' or "YES":
        print(f"Alright your birthday is {bDay}")

    elif reply == 'N' or "NO":
        PersonalInformation()

    else:
        print('I apologies, I did not catch that. Please repeat.')
        PersonalInformation()

#-------------------------------------------------------------------------

    # Age
    age = input("When is your birthday?: ")

    print(f"Your age is {age} is that correct?")

    reply = input().upper()

    if reply == 'Y' or "YES":
        print(f"Alright you are {age} years old")

    elif reply == 'N' or "NO":
        PersonalInformation()

    else:
        print('I apologies, I did not catch that. Please repeat.')
        PersonalInformation()

# -------------------------------------------------------------------------

    # Favorite color
    faveColor = input("What is your favorite color?: ")

    print(f"Your birthday is {faveColor} is that correct?")

    reply = input().upper()

    if reply == 'Y' or "YES":
        print(f"Alright your favorite color is {faveColor}")

    elif reply == 'N' or "NO":
        PersonalInformation()

    else:
        print('I apologies, I did not catch that. Please repeat.')
        PersonalInformation()

#-------------------------------------------------------------------------

introduction()

PersonalInformation()




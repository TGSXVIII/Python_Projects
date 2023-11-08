import time
import random

bfpoints = 0

def ask_question(question, options, correct_answer, bfpoints):
    print(question)
    time.sleep(2.5)

    print("Options:")

    for i, option in enumerate(options, 1):
        time.sleep(0.5)
        print(f"{i}. {option}")

    user_answer = input("Your answer: ").lower()
    time.sleep(1.5)

    if user_answer == correct_answer:
        print("That is the correct answer! Well done")
        bfpoints += 10

    else:
        print("That is not the correct answer")
        bfpoints -= 5
    time.sleep(1.5)

    return bfpoints

def myGame():
    usernames = ["Douchebag", "Cunt", "Ass Face", "Motherfucker", "Dickhead", "Bitch", "Prick", "Richard"]
    input("Hello user, please write your name: ")
    usernameFucked = usernames[random.randint(0, len(usernames) - 1)]

    time.sleep(0.5)
    print(f"So {usernameFucked} is your name?")

    time.sleep(0.5)
    input("Is this correct?: ")

    time.sleep(1)
    print(f"Alright {usernameFucked}, welcome to the brain fuck. We hope you have fun.")

    time.sleep(2.5)
    bfpoints = 0
    print(f"First of all, here are your current points: {bfpoints}")

    time.sleep(2.5)
    print("Now we will be asking you a couple of questions.")

    time.sleep(2.5)
    print("For every correct answer, you will receive 10 points, but every wrong answer you will be deducted  5 points.")

    time.sleep(2.5)
    print("You must answer the questions correctly to continue the game.")

    questions = [
        ("What is the name of the robot that was sent to earth in WALL-E?", ["Sonny", "Rosey", "Tron", "Eve"], "eve"),
        ("What did I have for dinner yesterday?", ["Burger", "Pizza", "Nothing", "A Unicorn"], 5),
        ("What is the meaning of life?", ["42", "69", "360", "420"], "42"),
        ("How many films are there in the Fast and Furious series?", ["3", "5", "10", "Way too many"], "way too many"),
        ("WHAT DO WE USE TO PURGE UNHOLY XENOS BROTHERS?", ["Bullets!", "Holy Hell Fire!", "Hell Fire!", "Fists!"], "holy hell fire")
    ]

    for q in questions:
        bfpoints = ask_question(q[0], q[1], q[2], bfpoints)

myGame()
import random
import time

def get_user_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in {'yes', 'no', 'y', 'n'}:
            return choice
        print("That is not a correct value")

def coin_toss():
    toss = get_user_choice("Do you want to flip the coin?: ")

    if toss == "no" or toss == "n":
        print("Thanks for playing")
        exit()

    print("Coin is flipping...")
    time.sleep(1.5)
    print("It is...")
    time.sleep(1)

    flip = random.choice(["Heads", "Tails"])
    print(flip)
    return flip

def main():
    record_list = []
    while True:
        result = coin_toss()
        record_list.append(result)
        if get_user_choice("Do you want to flip the coin again?: ") in {"no", "n"}:
            break

if __name__ == "__main__":
    main()

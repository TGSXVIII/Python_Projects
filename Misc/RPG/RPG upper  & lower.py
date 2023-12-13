import random
import string
import time

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_random_password(length):
    """
    Generate a random password of given length.
    """
    if length <= 0:
        raise ValueError("Password length should be a positive integer.")

    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list
    password = [random.choice(characters) for _ in range(length)]

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to string
    password_string = "".join(password)

    return password_string

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        print("Generating password...")
        time.sleep(1.5)

        password = generate_random_password(length)

        print("Your password is:")
        time.sleep(1.5)
        print(password)

    except ValueError as e:
        print(e)

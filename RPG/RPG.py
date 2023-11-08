import secrets
import string
import time

# Valid characters for the password
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def generate_random_password():
    # Length of the password from the user
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    print("Generating password...")
    time.sleep(1.5)

    # Generate the password using secrets.choice for security
    password = ''.join(secrets.choice(characters) for i in range(length))

    print("Your password is:")
    time.sleep(1.5)
    print(password)

# Invoking the function
generate_random_password()


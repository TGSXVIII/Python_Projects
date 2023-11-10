import time
import os


# Define the countdown function.
def countdown(t):
    while t:
        hours, rem = divmod(t, 3600)
        mins, secs = divmod(rem, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        print("Time Left: " + timer, end="\r")
        time.sleep(1)

        t -= 1

    print('\nFire in the hole!!')


# Clear the screen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def get_time_input():
    while True:
        try:
            user_input = input("Enter the time (e.g., '5s' for seconds, '10m' for minutes, '2h' for hours): ")
            if user_input[-1] not in ('s', 'm', 'h'):
                raise ValueError("Invalid input format")

            t = int(user_input[:-1])
            unit = user_input[-1]

            if unit == 's':
                t = t
            elif unit == 'm':
                t *= 60
            elif unit == 'h':
                t *= 3600

            if t < 0:
                raise ValueError("Time can't be negative!")
            return t
        except ValueError as e:
            print(f"Invalid input: {e}")


def repeat_timer():
    while True:
        clear()
        t = get_time_input()
        clear()
        countdown(t)
        repeat = input("Do you want to set another timer? (yes/no): ")
        if repeat.lower() != 'yes':
            break


# Main program
while True:
    repeat_timer()
    again = input("Do you want to run the timer again? (yes/no): ")
    if again.lower() != 'yes':
        break

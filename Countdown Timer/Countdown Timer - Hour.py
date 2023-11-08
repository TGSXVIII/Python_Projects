import time
import os

# define the countdown func.
def countdown(t):
    while t:
        hours, rem = divmod(t, 3600)
        mins, secs = divmod(rem, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

# Clear the screen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# input time in hours
while True:
    try:
        t = int(input("Enter the time in hours: ")) * 3600
        if t < 0:
            raise ValueError("Time can't be negative!")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

# function call
clear()
countdown(t)

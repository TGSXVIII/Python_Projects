# Import necessary libraries
import time
import pygame
import sys
import random
import tkinter as tk
from playsound import playsound

# Initialize Pygame
pygame.init()

# Load word list
word_list = ["python", "hangman", "game", "programming", "developer", "coding", "computer"]

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the size of the hangman images
IMAGE_WIDTH, IMAGE_HEIGHT = 200, 200

# Define fonts
FONT = pygame.font.SysFont(None, 55)

# Choose a random word
word = random.choice(word_list)
guessed_word = ['_' for _ in word]

# Initialize the set to store used letters
used_letters = set()

# Set up display
window = tk.Tk()
window.title('Hangman Game')

# Define the window display size
WIDTH, HEIGHT = 800, 600

# Create a label at the top of the window
l = tk.Label(window, bg='white', text='Welcome to Hangman!')
l.pack()

# Load hangman images with specified size
hangman_images = \
    [
        pygame.transform.scale(pygame.image.load(f"/Hangman/PyGame Hangman 2/Pictures/hangman{i}.jpg"), (IMAGE_WIDTH, IMAGE_HEIGHT)) for i in range(12)
    ]

# Game variables
incorrect_guesses = 0
max_attempts = len(hangman_images) - 1

# Function to start the game
def start_game():
    # Hide the main window
    window.withdraw()

    # Set up the Pygame window
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman Game")

    global word, guessed_word, used_letters, incorrect_guesses
    word = random.choice(word_list)
    guessed_word = ['_' for _ in word]
    used_letters = set()
    incorrect_guesses = 0
    game_loop(win)

# Function to quit the game
def quit_game():
    window.destroy()

# Create buttons for starting and quitting the game
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

quit_button = tk.Button(window, text="Quit Game", command=quit_game)
quit_button.pack()

# Function for the main game loop
def game_loop(win):
    global word, guessed_word, used_letters, incorrect_guesses

    # Main game loop
    while True:
        win.fill(WHITE)

        # Draw guessed word
        display_word = FONT.render(" ".join(guessed_word), True, BLACK)
        win.blit(display_word, ((WIDTH - display_word.get_width()) // 2, 400))

        # Draw used letters
        used_letters_text = FONT.render("Used Letters: " + " ".join(sorted(used_letters)), True, BLACK)
        win.blit(used_letters_text, ((WIDTH - used_letters_text.get_width()) // 2, 50))

        # Draw hangman image
        win.blit(hangman_images[incorrect_guesses], (300, 100))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key in range(97, 123):  # Check if a letter key is pressed
                    letter = chr(event.key)

                    # Check if the letter has not been used before
                    if letter not in used_letters:
                        used_letters.add(letter)  # Add the letter to the set

                        # Check if the letter pressed is a part of the word
                        if letter not in word:
                            incorrect_guesses += 1

                            # Check if the amount of incorrect guesses equals the max amount of guesses
                            if incorrect_guesses == max_attempts:
                                # Load and display the image
                                image = pygame.image.load(r"../PyGame Hangman 2/Pictures/you died.png")  # Use raw string or double backslashes
                                win.blit(image, ((WIDTH - image.get_width()) // 2, (HEIGHT - image.get_height()) // 2))
                                pygame.display.update()

                                playsound(r"../PyGame Hangman 2/Audio files/Voicy_YOU DIED .mp3")
                                time.sleep(1)

                                print("Game over! The word was:", word)
                                quit_game()
                        else:

                            # Update guessed_word with correct guesses
                            for i, char in enumerate(word):
                                if char == letter:
                                    guessed_word[i] = letter

        # Check for win
        if "_" not in guessed_word:
            # Load and display the image
            image = pygame.image.load(r"../PyGame Hangman 2/Pictures/victory.png")  # Use raw string or double backslashes
            win.blit(image, ((WIDTH - image.get_width()) // 2, (HEIGHT - image.get_height()) // 2))
            pygame.display.update()

            time.sleep(1)  # Adjust the time as needed

            playsound(r"../PyGame Hangman 2/Audio files/Voicy_freddy fazbear meme.mp3")
            time.sleep(1)  # Adjust the time as needed

            print("Congratulations! You guessed the word:", word)
            quit_game()

        pygame.display.update()

# Function to quit the game
def quit_game():
    pygame.quit()
    sys.exit()

# Start the Tkinter event loop
window.mainloop()

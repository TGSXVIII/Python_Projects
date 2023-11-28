# hangman_game.py
import time
import random
import pygame
from playsound import playsound
from Hangman_UI import *

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
WIDTH, HEIGHT = 800, 600
max_attempts = 11  # Maximum attempts for hangman images

# Load hangman images with specified size
hangman_images = [
    pygame.transform.scale(pygame.image.load(f"C:/Users/mads020n/OneDrive - mercantec/PycharmProjects/Hangman/PyGame Hangman/Pictures/hangman{i}.jpg"), (IMAGE_WIDTH, IMAGE_HEIGHT)) for i in range(12)
]

# Game variables
incorrect_guesses = 0


def game_loop(win, quit_game_callback):
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
                quit_game_callback()

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
                                image = pygame.image.load(r"Pictures\you died.png")  # Use raw string or double backslashes
                                win.blit(image, ((WIDTH - image.get_width()) // 2, (HEIGHT - image.get_height()) // 2))
                                pygame.display.update()

                                playsound(r"Audio files\Voicy_YOU DIED .mp3")
                                time.sleep(1)

                                print("Game over! The word was:", word)
                                quit_game_callback()
                        else:
                            # Update guessed_word with correct guesses
                            for i, char in enumerate(word):
                                if char == letter:
                                    guessed_word[i] = letter

        # Check for win
        if "_" not in guessed_word:
            # Load and display the image
            image = pygame.image.load(r"Pictures\victory.png")  # Use raw string or double backslashes
            win.blit(image, ((WIDTH - image.get_width()) // 2, (HEIGHT - image.get_height()) // 2))
            pygame.display.update()

            time.sleep(1)  # Adjust the time as needed

            playsound(r"Audio files\Voicy_freddy fazbear meme.mp3")
            time.sleep(1)  # Adjust the time as needed

            print("Congratulations! You guessed the word:", word)
            quit_game_callback()

        pygame.display.update()
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont(None, 55)

# Load word list
word_list = ["python", "hangman", "game", "programming", "developer", "coding", "computer"]

# Choose a random word
word = random.choice(word_list)
guessed_word = ['_' for _ in word]

# Hangman stages
hangman_images = [pygame.image.load(f"hangman_images/hangman{i}.png") for i in range(7)]

# Game variables
incorrect_guesses = 0
max_attempts = len(hangman_images) - 1

# Main game loop
while True:
    win.fill(WHITE)

    # Draw guessed word
    display_word = FONT.render(" ".join(guessed_word), True, BLACK)
    win.blit(display_word, (250, 400))

    # Draw hangman image
    win.blit(hangman_images[incorrect_guesses], (300, 100))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key in range(97, 123):  # Check if a letter key is pressed
                letter = chr(event.key)

                if letter not in word:
                    incorrect_guesses += 1

                    if incorrect_guesses == max_attempts:
                        # Game over - you can add more here
                        print("Game over! The word was:", word)
                        pygame.quit()
                        sys.exit()

                else:
                    for i, char in enumerate(word):

                        if char == letter:
                            guessed_word[i] = letter

    # Check for win
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
        pygame.quit()
        sys.exit()

    pygame.display.update()

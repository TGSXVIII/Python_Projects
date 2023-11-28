# hangman_ui.py
import tkinter as tk
import pygame
from Hangman_Game import *

def start_game():
    # Set up display
    window = tk.Tk()
    window.title('Hangman Game')

    # Create a label at the top of the window
    l = tk.Label(window, bg='white', text='Welcome to Hangman!')
    l.pack()

    # Create buttons for starting and quitting the game
    start_button = tk.Button(window, text="Start Game", command=lambda: start_game_internal(window))
    start_button.pack()

    quit_button = tk.Button(window, text="Quit Game", command=quit_game)
    quit_button.pack()

    # Start the Tkinter event loop
    window.mainloop()

def start_game_internal(window):
    # Hide the main window
    window.withdraw()

    # Set up the Pygame window
    pygame.init()
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hangman Game")

    game_loop(win, quit_game)
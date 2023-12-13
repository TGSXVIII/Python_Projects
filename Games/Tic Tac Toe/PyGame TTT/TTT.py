import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the game state
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = ''


def draw_grid():
    # Draw horizontal lines
    for i in range(1, 3):
        pygame.draw.line(window, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)

    # Draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(window, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // (HEIGHT // 3)
    col = x // (WIDTH // 3)
    return int(row), int(col)


def draw_xo(row, col):
    font = pygame.font.Font(None, 120)
    text = font.render(board[row][col], True, WHITE)
    text_rect = text.get_rect(center=(col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6))
    window.blit(text, text_rect)


def check_winner():
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == current_player or \
                board[0][i] == board[1][i] == board[2][i] == current_player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == current_player or \
            board[0][2] == board[1][1] == board[2][0] == current_player:
        return True
    return False


def is_board_full():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


def restart_game():
    global board, current_player
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = ''


def computer_move():
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    return random.choice(available_moves)


def main():
    global current_player
    current_player = ''
    first = True
    while True:
        if first:
            current_player = 'X'
            first = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
                    row, col = get_row_col_from_mouse(pygame.mouse.get_pos())

                    if board[row][col] == '' and not check_winner():
                        board[row][col] = current_player

                        if check_winner():
                            print(f"Player {current_player} wins!")
                            restart_game()

                        elif is_board_full():
                            print("It's a draw!")
                            restart_game()

                        else:
                            if current_player == 'X':
                                current_player = 'O'

                            else:
                                current_player = 'X'

                        # Computer move
                        if not check_winner() and not is_board_full():
                            computer_row, computer_col = computer_move()
                            board[computer_row][computer_col] = current_player

                            if check_winner():
                                print("Computer wins!")
                                restart_game()

                            elif is_board_full():
                                print("It's a draw!")
                                restart_game()

                            else:
                                if current_player == 'X':
                                    current_player = 'O'
                                else:
                                    current_player = 'X'

        window.fill(BLACK)
        draw_grid()

        # Draw X and O based on the game state
        for i in range(3):
            for j in range(3):
                if board[i][j] != '':
                    draw_xo(i, j)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()

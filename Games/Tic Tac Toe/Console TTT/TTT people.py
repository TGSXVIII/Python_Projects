import time

# Define the game board
game_board = [' ' for _ in range(10)]

def display_board(board):
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("     |     |     ")

def check_valid_input(player_input):
    return player_input.lower() in ['x', 'o']

def check_valid_position(position):
    return position.isdigit() and 1 <= int(position) <= 9 and game_board[int(position)] == ' '

def check_win(board, mark):
    win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

def is_board_full(board):
    return all(x != ' ' for x in board[1:])

def play_again():
    while True:
        decision = input("Do you want to play again? (yes/no): ").strip().lower()
        if decision in ['yes', 'no']:
            return decision == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def TTT():
    global game_board
    print("Player 1 will be 'O' and Player 2 will be 'X'")

    print("Player 1, please write your name: ")
    playerOne = input()

    print("Player 2, please write your name: ")
    playerTwo = input()

    display_board(game_board)

    while True:
        playerOneSelect = 'o'
        playerTwoSelect = 'x'

        while True:
            position = input(f"{playerOne}, select a position (1-9): ").strip()
            if check_valid_position(position):
                game_board[int(position)] = playerOneSelect
                display_board(game_board)
                if check_win(game_board, playerOneSelect):
                    print(f"Congratulations! {playerOne} has won!")
                    if not play_again():
                        return
                    game_board = [' ' for _ in range(10)]
                    display_board(game_board)
                    break
                if is_board_full(game_board):
                    print("It's a tie! The board is full.")
                    if not play_again():
                        return
                    game_board = [' ' for _ in range(10)]
                    display_board(game_board)
                    break
                break
            print("Invalid position. Please try again.")

        while True:
            position = input(f"{playerTwo}, select a position (1-9): ").strip()
            if check_valid_position(position):
                game_board[int(position)] = playerTwoSelect
                display_board(game_board)
                if check_win(game_board, playerTwoSelect):
                    print(f"Congratulations! {playerTwo} has won!")
                    if not play_again():
                        return
                    game_board = [' ' for _ in range(10)]
                    display_board(game_board)
                    break
                if is_board_full(game_board):
                    print("It's a tie! The board is full.")
                    if not play_again():
                        return
                    game_board = [' ' for _ in range(10)]
                    display_board(game_board)
                    break
                break
            print("Invalid position. Please try again.")

TTT()

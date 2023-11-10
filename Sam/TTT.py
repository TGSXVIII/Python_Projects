import random

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

def computer_move(board, computer_mark):
    available_moves = [i for i in range(1, 10) if board[i] == ' ']
    return random.choice(available_moves)

def TTT():
    global game_board
    print("You will be 'O', and the computer will be 'X'.")

    print("Player, please write your name: ")
    player = input()

    display_board(game_board)

    while True:
        playerSelect = 'o'
        computerSelect = 'x'

        while True:
            position = input(f"{player}, select a position (1-9): ").strip()
            if check_valid_position(position):
                game_board[int(position)] = playerSelect
                display_board(game_board)
                if check_win(game_board, playerSelect):
                    print(f"Congratulations! {player} has won!")
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

        computer_position = computer_move(game_board, computerSelect)
        game_board[computer_position] = computerSelect
        display_board(game_board)

        if check_win(game_board, computerSelect):
            print("The computer has won! Better luck next time.")
            if not play_again():
                return
            game_board = [' ' for _ in range(10)]
            display_board(game_board)
            continue

        if is_board_full(game_board):
            print("It's a tie! The board is full.")
            if not play_again():
                return
            game_board = [' ' for _ in range(10)]
            display_board(game_board)
            continue

TTT()

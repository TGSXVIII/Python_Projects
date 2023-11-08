while True:
    player1 = input("Player 1, enter your name: ").lower()
    print(f"Hello {player1}! Welcome to Rock, Paper, Scissors.")

    player2 = input("Player 2, enter your name: ").lower()
    print(f"Hello {player2}! Welcome to Rock, Paper, Scissors.")

    while True:
        print(f"{player1}, pick either Rock, Paper, or Scissors")
        input1 = input().lower()

        print(f"{player2}, pick either Rock, Paper, or Scissors")
        input2 = input().lower()

        options = ["rock", "paper", "scissors"]

        if input1 not in options or input2 not in options:
            print("Please enter a valid option (Rock, Paper, or Scissors)!")
        else:
            if input1 == input2:
                print("Tie!")
            elif (input1 == "rock" and input2 == "paper") or (input1 == "paper" and input2 == "scissors") or (input1 == "scissors" and input2 == "rock"):
                print(f"{player2} wins! {input2} beats {input1}")
            else:
                print(f"{player1} wins! {input1} beats {input2}")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

    play_again_main = input("Do you want to play another round? (yes/no): ").lower()
    if play_again_main != "yes":
        break

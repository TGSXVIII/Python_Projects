#Plader is a dictionary
#The names are strings
#The number (values) are strings
plader = {
    "Mathias": [[2, 42, 62, 71, 83], [6, 23, 35, 68, 88], [7, 18, 24, 55, 69]],
    "Tinna": [[13, 23, 30, 52, 83], [3, 24, 45, 63, 75], [9, 47, 56, 69, 88]],
    "Lukas": [[3, 21, 30, 44, 52], [4, 45, 55, 77, 84], [14, 28, 69, 78, 86]],
    "Casper": [[10, 22, 50, 60, 83], [15, 35, 44, 51, 84], [9, 37, 58, 68, 79]],
    "Theodor": [[1, 10, 20, 43, 86], [16, 56, 63, 74, 89], [39, 45, 57, 64, 76]],
    "Dylan": [[11, 20, 33, 60, 72], [35, 42, 67, 77, 87], [7, 25, 59, 68, 88]],
    "Kris": [[20, 32, 50, 72, 80], [4, 17, 21, 33, 52], [8, 18, 34, 48, 66]],
    "Lau": [[1, 11, 32, 40, 50], [23, 36, 42, 63, 86], [28, 38, 49, 59, 77]],
    "Peter": [[13, 32, 41, 51, 85], [15, 22, 42, 74, 86], [9, 28, 37, 57, 68]],
}

print (f"You have {len(plader)} plates")

#This is used to check the values in one row
array = []
def numbersChoosenOne():
    number = int(input("Type the number here 1: "))
    array.append(number)
    print(array)
    for i in plader.keys():
        for k in range(0, 3):
            if all(x in array for x in plader[i][k]):
                print("You got a full row congratulations!")
                print("The plate ID: " + str(i))
                print("The plate numbers " + str(plader[i][k]))
                print("Would you like to keep playing for the second row for more rewards?")
                numbersChoosenTwo()
    numbersChoosenOne()

#This is used to check for the second row
def numbersChoosenTwo():
    number = int(input("Type the number here 2: "))
    array.append(number)
    print(array)
    for i in plader.keys():
        if all(x in array for x in plader[i][0]) and all(x in array for x in plader[i][1]) or all(x in array for x in plader[i][1]) and all(x in array for x in plader[i][2]) or all(x in array for x in plader[i][2]) and all(x in array for x in plader[i][0]):
            print("The plate ID: " + str(i))
            print("The plate numbers " + str(plader[i]))
            print("You got two full rows congratulations!")
            print("Would you like to keep playing for the whole plate for more rewards?!")
            numbersChoosenAll()
    numbersChoosenTwo()

#This checks for a whole plate
def numbersChoosenAll():
    number = int(input("Type the number here 3: "))
    array.append(number)
    print(array)
    for i in plader.keys():
        if all(x in array for x in plader[i][0]) and all(x in array for x in plader[i][1]) and all(x in array for x in plader[i][2]):
            print("The plate ID: " + str(i))
            print("The plate numbers " + str(plader[i]))
            print("You got the whole plate congratulations!")
            exit()
            numbersChoosenAll()
    numbersChoosenOne()

#When the game is over you can choose to play again or end the game
def Replay():
    print('Do you want to play again? [Y/N]')
    reply = input().lower()
    if reply == 'y':

    elif reply == 'n':
        exit()
    else:
        print("I apologies, I did not catch that. Please try again.")
        Replay()

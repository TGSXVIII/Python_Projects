#Loop back to this point once code finishes

loop = 1

while (loop < 10):

    # All the questions that the program asks the user

    maleName = input("Choose a male name: ")

    b_noun = input("Choose a noun (beginning with b): ")

    noun = input("Choose a noun: ")

    femaleName = input("Choose a female name: ")

    place = input("Name a place: ")

    action = input("Choose an action: ")

    action2 = input("Choose an action: ")

    action3 = input("Choose an action: ")

    famousPerson = input("Choose a famous person: ")

    #Displays the story based on the users input

    print ("------------------------------------------")

    print ("There was once a monkey that was named",maleName,"and he was a",b_noun,)

    print ("One day",maleName,"Was out hunting and found a",noun,)

    print ("While he was out he found a female monkey her name was",femaleName,)

    print ("They then went to",place,"and they",action,)

    print ("Then a lion came along and tried to",action2,femaleName,)

    print ("The male monkey then",action3,"the lion")

    print ("And",famousPerson,"filmed all of it")

    print ("------------------------------------------")

    # Loop back to "loop = 1"

    loop = loop + 1
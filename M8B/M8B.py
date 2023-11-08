import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('  __  __          _____ _____ _____    ___   _____        _ _')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \  |  _ \      | | |')
print(' | \  / |  /  \ | |  __  | || |      | (_) | | |_) | __ _| | |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ <  |  _ < / _` | | |')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) | | |_) | (_| | | |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/  |____/ \__,_|_|_|')
print('')

user = input('Hello, I am the Magic 8 Ball, What is your name?: ')
print(f"Hello {user} ask a question: ")

def Magic8Ball():
    question = input()

    if question == "what is the meaning with life":
        print("42")
        Replay()

    if question == "is racism funny":
        print("Hell yeah brother! XD")
        Replay()

    if question == "do women have rights":
        print("PFFFF hell nah!")
        Replay()

    else:
        print(answers[random.randint(0, len(answers) - 1)])
        print('I hope that helped!')
        Replay()

def Replay():
    print('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'y':
        print("ask me a question")
        Magic8Ball()
    elif reply == 'n':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()

Magic8Ball()
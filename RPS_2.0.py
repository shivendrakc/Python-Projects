import random

def play():
    user = input("Enter r for rock p for paper and s for scissor :")
    computer = random.choice(['r','s','p'])

    if user == computer:
        print("it's a tie")
    elif user == 'r' and computer == 's' or user == 'p' and computer == 'r' or user == 's' and computer == 'p':
        print("you won")
    else:
        print("you lost")


confirm = 'Y'
while confirm == 'Y':
    play()
    confirm = input("Do you want to play again Y/N?\n").upper()
else:
    print('Goodbye!')

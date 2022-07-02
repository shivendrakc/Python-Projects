import random

def play():
    user = input("What's your choice 'r' for rock, 's' for sisscor, 'p' for paper\n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "It's a tie"
    
    if IF_won(user, computer):
        return "you won"

    return "you lose" 
    
def IF_won(player, opponent):
    if player == 's' and opponent == 'p' or  player == 'p' and opponent == 'r' \
    or player == 'r' and opponent == 's':
        return True

print(play())
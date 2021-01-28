import random

# def play():
#     pl_choice = input("Enter your choice 'r' or 'p' or 's': ").lower()
#     comp_choice = random.choice(['r', 'p', 's'])
#     res = is_win(pl_choice, comp_choice)
#     if res:
#         print("You Win !")
#     else:
#         print("You Lose !")

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') and (player == 'p' and computer == 'r'):
        return True


res = False
while not res:
    pl_choice = input("Enter your choice 'r' or 'p' or 's': ").lower()
    comp_choice = random.choice(['r', 'p', 's'])
    res = is_win(pl_choice, comp_choice)
    if res:
        print("You Win !")
        break
    else:
        print("You Lose !")

print("Congrats You won !")
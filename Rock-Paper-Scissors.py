import random


def play():
    user_pick = input("Pick one: 'r' for rock, 'p' for paper, 's' for scissors\n")
    options = ('r', 'p', 's')
    computer_pick = random.choice(options)

    if user_pick == computer_pick:
        return 'it\'s a tie oh'

    # r > s, s > p, p > r
    if is_won(user_pick, computer_pick):
        return 'You won'

    if invalid(user_pick, options):
        return 'Invalid input'

    return 'You lost, ndo'


def is_won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


def invalid(player, choice):
    if player not in choice:
        return 'True'


print(play())

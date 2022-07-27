import random


# user guesses the correct number


def guess(x):
    random_number = random.randint(1, x)
    pick = 0
    while pick != random_number:
        pick = int(input(f'Guess a number between 1 and {x}: '))
        if pick < random_number:
            print('Sorry! Too low. Pick another number')
        elif pick > random_number:
            print('Oops! Too high. Pick another number')
    print(f'Yes! You picked the right number {random_number} correctly')


guess(10)


# computer guesses the correct number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            pick = random.randint(low, high)
        else:
            pick = low
        feedback = input(f'Is {pick} too high(h), too low(l) or correct(c):  ')
        if feedback == 'h':
            high = pick - 1
        elif feedback == 'l':
            low = pick + 1

        print(f'Yes!, you guessed the number {pick} correctly!')


computer_guess(15)

# For passing linting and static

'''From number 1-20, pick a GUESS that the prog has
randomly selected, if correct win $5, wrong lose $1.
Can try as many times until want to quit.'''

import random
import sys


def betting_game() -> None:

    BALANCE = 0
    CHOSEN = random.randint(1, 6)
    GUESS = input('\nYour GUESS (q to quit): ')

    if GUESS == 'q':
        sys.exit()
    else:
        pass
    if int(GUESS) == CHOSEN:
        BALANCE += 5
    else:
        BALANCE -= 1
    print('Guessed: {} ANSWER: {}'.format(GUESS, CHOSEN))
    print('Current  BALANCE: $', BALANCE)


START = input('I will randomly pick a number between 1-6\n\
Guess it correctly & gain $5. Wrong, lose $1.\n\
Ready to play? (y/n) ')

if START == 'n':
    sys.exit()
else:
    while True:
        betting_game()

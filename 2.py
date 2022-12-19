from random import randint
import sys

def guess():
    answer = randint(1,10)

    while True:

        try:

            user_guess = int(input('What is your guess?: '))

            if user_guess == answer:
                print('You guessed it.')
                break

            elif user_guess != answer:
                print('Not correct. Try again.')

        except ValueError:
            print('That is not a valid input')


guess()

# Guess the number
from random import randint
from art import logo


easy_level = 5
hard_level = 10

def guessing(guess, answer, turns):
    # guessed = int(input('Enter you guess: '))
    if guess == answer:
        print('You won')
    elif guess > answer:
        print('Too high')
        return turns - 1
    elif guess < answer:
        print('Too low')
        return turns - 1

def difficulty():
    level = input('Choose a difficulty. Type"hard" or "easy"\n').lower()
    if level == 'hard':
        return easy_level
    else:
        return hard_level
    
def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('Am thinking of a number between 1 and 100')
    answer = randint(0, 100)
    print(f'{answer} is the answer')

    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f'You have {turns} attepts remaing')
        guess = int(input('Make a guess: '))
        turns = guessing(guess, answer, turns)
        if turns == 0:
            print('You lose')
            return
        elif guess != answer:
            print('Guess again')

game()
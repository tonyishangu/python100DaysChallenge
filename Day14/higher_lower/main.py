from art import logo, vs
from game_date import data
import random
from replit import clear

def format_data(acc):
    '''formart the data'''
    acc_name = acc['name']
    acc_desc = acc['description']
    acc_country = acc['country']
    # acc_followers = acc_a['follower_count']
    return f'{acc_name}, a {acc_desc}, from {acc_country}'

def check_answer(choice, a_followers, b_followers):
    '''use if statement to check if user is correct'''
    if a_followers > b_followers:
        return choice == 'a'
    else:
        return choice == 'b'

# score keeping  
score = 0
# display art
print(logo)

# make game repeatable
game_still_on =  True
acc_b = random.choice(data)

while game_still_on:
    # generate 2 random accounts from the data
    acc_a = acc_b
    acc_b = random.choice(data)
    while acc_a == acc_b:
        acc_b = random.choice(data)

    # formated data
    print(f'Compare A: {format_data(acc_a)}')
    print(vs)
    print(f'Against B: {format_data(acc_b)}')

    # input guess
    choice = input('Who has more follers, A or B ?').lower()
    
    # check if user is correct
    # ##----get followers
    a_follower_count = acc_a['follower_count']
    b_follower_count = acc_b['follower_count']

    # ---/check if user is correct
    is_correct = check_answer(choice, a_follower_count, b_follower_count)

        # clear screen between rounds
    clear()
    print(logo)

    # give user feedback
    if is_correct:
        score += 1
        print(f'You are right, your score is {score}')
    else:
        game_still_on = False
        print(f'You are wrong haha!!!, Total score is {score}')
    


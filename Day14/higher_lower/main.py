from art import logo, vs
from game_date import data
import random


def format_data(acc):
    '''formart the data'''
    acc_name = acc['name']
    acc_desc = acc['description']
    acc_country = acc['country']
    # acc_followers = acc_a['follower_count']
    return f'{acc_name}, a {acc_desc}, from {acc_country}'

# display art
print(logo)
# generate 2 random accounts from the data
acc_a = random.choice(data)
acc_b = random.choice(data)
if acc_a == acc_b:
    acc_b = random.choice(data)

# formated data
print(f'Compare A: {format_data(acc_a)}')
print(vs)
print(f'Compare B: {format_data(acc_b)}')


# input guess
# check if user is correct
# ##----get folloers
#  ###use if statement to check if user is correct
# give user feedback
# score keeping
# make game repeatable
# clear screen between rounds
from art import logo, vs
from game_date import data
import random
# display art
print(logo)
# generate 2 random accounts from the data
acc_a = random.choice(data)
acc_b = random.choice(data)
if acc_a == acc_b:
    acc_b = random.choice(data)

# formart the data
acc_name = acc_a['name']
acc_desc = acc_a['description']
acc_country = acc_a['country']
acc_followers = acc_a['follower_count']
# input guess
# check if user is correct
# ##----get folloers
#  ###use if statement to check if user is correct
# give user feedback
# score keeping
# make game repeatable
# clear screen between rounds
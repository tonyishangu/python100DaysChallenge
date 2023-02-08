from art import logo, vs
from data import data
import random

print(logo)
print(data[0])
score = 0
game_over = False
while not game_over:
    person_a = random.choice(data)
    person_b = random.choice(data)
    char_a = person_a['name']
    char_b = person_b['name']
    a_desc = person_a['description']
    b_desc = person_b['description']
    num_a = person_a['follower_count']
    num_b = person_b['follower_count']
    print(f'Compare A: {char_a}, {a_desc}')
    print(vs)
    print(f'Compare B: {char_b}, {b_desc}')
    choice = input('Who has more follers, A or B ?').lower()

    if choice == 'a' and num_a > num_b:
        score += 1
        print(f'You are right! Current Score is {score}')
    elif choice == 'b' and num_b > num_a:
        score += 1
        print(f'You are right! Current Score is {score}')
    else:
        game_over = True
        print(f'wrong, Your total score is {score}')
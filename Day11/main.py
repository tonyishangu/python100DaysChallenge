from art import logo
import random

print(logo)
def pick_card():
    '''returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

dealer_card = []
player_card = []

for _ in range(2):
    player_card.append(pick_card())
    dealer_card.append(pick_card())

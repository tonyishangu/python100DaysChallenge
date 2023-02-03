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

def calc_score(cards):
    '''return sum of the cards dealed'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

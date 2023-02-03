from art import logo
import random

print(logo)
def pick_card():
    '''returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    '''return sum of the cards dealed'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
         
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return 'Draw'
    elif dealer_score == 0:
        return 'Dealer Wins with a Blackjack'
    elif player_score == 0:
        return 'Player Wins with a Blackjack'
    elif player_score > 21:
        return 'Above 21 you lose'
    elif dealer_score > 21:
        return 'Dealer went above 21 you win'
    elif player_score > dealer_score:
        return 'Pplayer Wins'
    else:
        return 'You lose'

dealer_card = []
player_card = []
game_over = False

for _ in range(2):
    player_card.append(pick_card())
    dealer_card.append(pick_card())
    print(f'player cards {player_card}')
    print(f'dealer cards {dealer_card[0]}')
while not game_over:
    player_score = calc_score(player_card)
    dealer_score = calc_score(dealer_card)
    print(f'player score: {player_score}')
    print(f'dealer score: {dealer_score}')

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        game_over = True
    else:
        player_deal = input('Type "y" to get a new card or "n" to pass\n').lower()
        if player_deal == 'y':
            player_card.append(pick_card())
            player_score = calc_score(player_card)
            print(f'new score: {player_card}')
            print(player_score)
        else:
            game_over = True
while dealer_score != 0 and dealer_score < 17:
    dealer_card.append(pick_card())
    dealer_score = calc_score(dealer_card)

print(compare(player_score, dealer_score))
import random

words = ['advert', 'apple', 'zebra', 'academy', 'fox']

end_game = False
while not end_game:
    choosen_word = random.choice(words)

    print(choosen_word)
    length = len(choosen_word)
    print(length)
    display = []

    for _ in range(length):
        display += '_'
    print(display)

    guess = input('Guess a letter\n').lower()

    for pos in range(length):
        letter = choosen_word[pos]
        if letter == guess:
            display[pos] = letter

    print(display)

    if '_' not in display:
        end_game = True
        print('You won')
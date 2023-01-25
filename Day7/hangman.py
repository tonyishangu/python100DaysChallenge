import random

words = ['advert', 'apple', 'zebra', 'academy', 'fox']
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
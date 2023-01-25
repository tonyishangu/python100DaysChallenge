import random

words = ['advert', 'apple', 'zebra', 'academy', 'fox']
choosen_word = random.choice(words)
print(choosen_word)
guess = input('Guess a letter\n')
for i in choosen_word:
    if i == guess:
        print(i)
    else:
        print('nope')
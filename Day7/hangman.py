import random
import art
# from art import logo, stages
import guess_words
# from guess_words import words

print(art.logo)
end_game = False
choosen_word = random.choice(guess_words.words)
length = len(choosen_word)
print(length)

lives = 6
print(choosen_word)

display = []

for _ in range(length):
    display += '_'
print(display)

while not end_game:
    guess = input('Guess a letter\n').lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(length):
        letter = choosen_word[pos]

        if letter == guess:
            display[pos] = letter

    if guess not in choosen_word:
        print(f"Your guess of {guess} is wrong")
        lives -= 1
        if lives == 0:
            end_game = True
            print('You lose dummy')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_game = True
        print('You won')

    print(art.stages[lives])
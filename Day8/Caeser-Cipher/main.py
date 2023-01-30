alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(p_text, shift_no):
    word = ''
    for letter in p_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift_no
        new_letter = alphabet[new_pos]
        word += new_letter
    print(f'encoded word is {word}')

def decryt(enc_word, shift_num):
    new_word = ''
    for letters in enc_word:
        position = alphabet.index(letters)
        new_position = position - shift_num
        new_word += alphabet[new_position]
    print(f'decoded word is {new_word}')

if direction == 'encode':
    encrypt(p_text=text, shift_no=shift)
elif direction == 'decode':
    decryt(enc_word=text, shift_num=shift)
else:
    print('Wrong input')
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_of_letters = int(input('Enter number of letters you want in your password\n'))
num = int(input('enter the number of numbers you want in your password\n'))
sbl = int(input('Enter the number of symbols you want in your password\n'))

# ltr = random.sample(letters, no_of_letters)
# numb = random.sample(numbers, num)
# symbol = random.sample(symbols, sbl)
# password_list = ltr + numb + symbol
# psw = ''
# for i in password_list:
#     psw = psw + i
# print(psw)

# password = ''
# for char in range(1, no_of_letters + 1):
#     password += random.choice(letters)
# for char in range(1, num + 1):
#     password += random.choice(numbers)
# for char in range(1, sbl + 1):
#     password += random.choice(symbols)
# print(password)


# shuffled password
password = []
for char in range(1, no_of_letters + 1):
    password.append(random.choice(letters))
for char in range(1, num + 1):
    password.append(random.choice(numbers))
for char in range(1, sbl + 1):
    password.append(random.choice(symbols))
print(password)
random.shuffle(password)
print(password)
my_password = ''
for char in password:
    my_password += char
print(my_password)
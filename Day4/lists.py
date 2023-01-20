import random


counties = ['Nairobi', 'Kiambu', 'Kajiado', 'Machakos']
counties.append('Nakuru')
counties.extend(['Narok', 'Kisumu', 'Malindi', 'Meru'])
# counties.pop()
length = len(counties)
print(length)
print(counties)

# Banker Roulette
# input.split(',')

names = ['Tony', 'Michelle', 'Alex', 'Racheal']
one_to_pay = random.randint(0, len(names))
print(f'{names[one_to_pay - 1]} is paying for diner today')
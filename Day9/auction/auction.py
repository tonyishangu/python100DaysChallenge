import os
from art import logo

print(logo)

name = input('enter your name\n')
bid = int(input('Enter your bid\n'))
entry = {
    'names':name,
    'bids': bid
}
# def add_dict(names, bids):
#     entry = {
#         'name':names,
#         'bid': bids
#     }
#     print(entry)

# add_dict(name, bid)
print(entry)
more_bids = input('Are there any more bids. Yes or No\n').lower()
if more_bids == 'no':
    for b in entry:
        print(entry[b])
else:
    print('over')
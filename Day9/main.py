# dictionary
# key value pair
# syntax
#   {key: value}

programming_dictionary = {
    'Bug': 'An error in programming',
    'function': 'Code that can easily be called more than once',
}

# fetching from dictionary
# print(programming_dictionary['Bug']) # using a key

# Adding to the dictionary
programming_dictionary['loop'] = 'Doing something over and over again'
# print(programming_dictionary)

# empty dictionary
empty_dict = {}

# wipe a existing dictionary
    # programming_dictionary = {}
    # print(f'new dictionary: {programming_dictionary}')

# edit a dictionary
programming_dictionary['Bug'] = 'Something developers hate expecially on a friday'
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
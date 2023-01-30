def greet():
    print('hello')
    print('I said hello')
    print('Nice one')

greet()

def greet_with_name(name):
    print(f'hello {name}')

greet_with_name('Tony')

def greet_with(name, location):
    print(f'hello {name}')
    print(f'what is it like staying at {location}')

greet_with('Tony', 'kikuyu')  #positioonal arguements
greet_with(location='Kikuyu', name='Tony Ishangu') #keyword arguements

def paint_calc(height,width,cover):
    num_of_cans = round((height * width)/cover)
    print(f'you need {num_of_cans} cans')

h = int(input('Enter the heigth\n'))
w = int(input('Enter the width\n'))
coverage = 5
paint_calc(height=h, width=w, cover=coverage )

# FUNCTIONS WITH OUTPUT
# def mu_function():
#   result = a*b
#   return result
f_name = input('enter your first name\n')
l_name = input('enter your last name\n')

# def format_name(f_name, l_name):
#     first = f_name.title()
#     last = l_name.title()
#     name = f'{first} {last}'
#     print(name)
#     return name

# format_name(f_name=f_name, l_name=l_name)

# MULTIPLE RETURNS

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return print('invalid input')
    first = f_name.title()
    last = l_name.title()
    name = f'{first} {last}'
    print(name)
    return name

format_name(f_name=f_name, l_name=l_name)
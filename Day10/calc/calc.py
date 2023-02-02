from art import logo

print(logo)

# Adding Function
def add(a, b):
    return a + b

# Subtract Function
def minus(a, b):
    return a - b

# Multiplication Function
def multiply(a, b):
    return a * b

# division Function
def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': minus,
    '*': multiply,
    '/': divide
}

a = int(input('Enter the first number'))

for ops in operations:
    print(ops)

pick_ops = input('Pick an operation from the list above')
b = int(input('Enter the second number'))

calc_func = operations[pick_ops]
answer = calc_func(a, b)

print(f'{a} {pick_ops} {b} = {answer}')
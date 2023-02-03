from art import logo

# Adding Function
def add(num1, num2):
    return num1 + num2

# Subtract Function
def minus(num1, num2):
    return num1 - num2

# Multiplication Function
def multiply(num1, num2):
    return num1 * num2

# division Function
def divide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': minus,
    '*': multiply,
    '/': divide
}
def calculator():
    print(logo)
    num1 = float(input('Enter the first number\n'))
    for ops in operations:
        print(ops)
    should_continue = True

    while should_continue:
        pick_ops = input('Pick an operation\n')
        num2 = float(input('Enter the second number\n'))
        calc_func = operations[pick_ops]
        answer = calc_func(num1, num2)

        print(f'{num1} {pick_ops} {num2} = {answer}')

        if input(f'Type "y" if you want to continue the calculation using {answer} or "n" to start a new calculation\n') == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

    # pick_ops = input('Pick another operator')
    # num3 = int(input('Enter another number'))
    # calc_func = operations[pick_ops]
    # second_answer = calc_func(calc_func(num1, num2), num3)

    # print(f'{answer} {pick_ops} {num3} = {second_answer}')
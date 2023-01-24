# syntax
# while something is true:
#     do something repeatedly
x = 10
while x > 0:
    x -= 1
    print(x)


y = 100
while y > 0:
    if y % 5 == 0 and y % 3 == 0:
        print('fizzbuzz')
    elif y % 3 == 0:
        print('fizz')
    elif y % 5 == 0:
        print('buzz')
    else:
        print(y)
    y -= 1
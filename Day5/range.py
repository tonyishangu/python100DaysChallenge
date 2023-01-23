# syntax 
# for number in range(a, b, c=>step):
    # print(number)

# calc the sum of every even number between 1 and 101
total = 0
for i in range (1, 101):
    if i % 2 == 0:
        total += i
print(total)
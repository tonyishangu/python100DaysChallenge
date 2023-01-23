fruits = ['Apples', 'Banana', 'Pineapple', 'Mango']

for fruit in fruits:
    print(fruit)
# calcualte average height without using len and sum and round off to whole digit
heights = [123, 134, 128, 131, 145, 164]
total = 0
counter = 0
avg = 0
for h in heights:
    total = total + h
    counter += 1
avg = round(total/counter)
print(avg)

# calculate the max number in a list
scores = [78, 65, 89, 86, 55, 91, 64, 89]
cur_max = scores[0]
for s in scores:
    if s > cur_max:
        cur_max = s
print(f'score is {s}')

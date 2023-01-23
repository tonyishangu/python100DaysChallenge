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
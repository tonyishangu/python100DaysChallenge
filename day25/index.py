import pandas

data = pandas.read_csv('SquirrelData.csv')
graySQ = data[data['Primary Fur Color'] == 'Gray']
# print(graySQ)

print('*******************************************************************')
# get count of graySQ
gray_count = len(graySQ)
print(gray_count)

redSQ = data[data['Primary Fur Color'] == 'Cinnamon']
red_count = len(redSQ)
print(red_count)

blackSQ = data[data['Primary Fur Color'] == 'Black']
black_count = len(blackSQ)
print(black_count)

print('*******************************************************************')
# creating a new dataframe
data_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'count': [gray_count, red_count, black_count]
}

sqframe = pandas.DataFrame(data_dict)
sqframe.to_csv('sqcount.csv')
print(sqframe)
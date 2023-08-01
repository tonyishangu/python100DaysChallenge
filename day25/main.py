                # READING FILE
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

                # USING CSV
# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#     #print temparatures 
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

                # USING PANDAS
import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
print(data['temp'])

data_dict = data.to_dict()   #converts to a dictionary
print('dict', data_dict)

data_list = data['temp'].to_list()      #converts to a list
print('list', data_list)

# average temp using the list
avg = sum(data_list)/len(data_list)
print(f'average temp is {avg}')

# using pandas
print (data['temp'].mean())

# max value using pandas
print(data['temp'].max())

# get data in columns
print(data['condition'])
print(data.condition)

print('*******************************************************************')

# get data in row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

print('*******************************************************************')
monday = data[data.day == 'Monday']
print(monday.condition)

print('*******************************************************************')
tempIn_f = (monday.temp * 9/5) + 32
print(tempIn_f)

print('*******************************************************************')

                # CREAT A DATAFRAME
dict_data = {
    'students': ['amy', 'james', 'Brian'],
    'scores': [76, 57, 82]
}
dataframe = pandas.DataFrame(dict_data)
print(dataframe)
dataframe.to_csv('scores.csv')
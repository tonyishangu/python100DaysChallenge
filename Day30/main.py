# errors
# catching exeptions

# file not found
# with open('file.txt') as file:
#     file.read()     #file does not exist

# # key error
# dictionary = {'key':'value'}
# value = dictionary['non_existent_key']      #key does not exist

# # index error
# fruits_list = ['Apple', 'Banana', 'Pear']
# fruit = fruits_list[3]      #wrong index provided

# # type error
# a='one'
# b=2
# print(a+b)

# using try and except
try:
    file = open("file1")
    a_dict = {'key':'value'}
    print(a_dict['fwfew'])
except FileNotFoundError:
    file = open('file.txt', 'w')
    file.write('hello Tony')
except KeyError as error_message:
    print (f'Key {error_message} Error Occured!')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file closed')
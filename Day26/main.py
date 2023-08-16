# list comprehension

# new_list = [new_item for item in list]

# TODO:example using for loop
nums = [1,2,3]
new_list = []
for n in nums:
    add_1 = n + 1
new_list.append(add_1)

# TODO: example using list comprehension

new = [n + 1 for n in nums]
print(new)

name = 'Tony'
neww = [n for n in name]
print(neww)

range(1,5)
new_range = [r*2 for r in range(1,5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [nm for nm in names if len(nm) < 5]
caps_names = [ nm.upper() for nm in names if len(nm) > 5]
print(short_names)
print(caps_names)


# conditional Dictionary Comprehension

# TODO: dict_comp = {new_kwy:new_value for item in list}
# TODO:create dictionary comprehension from names array

# student_scores = {
#     'Alex': 89,
#     'Beth': 92,
#     'Caroline': 87,
#     'Dave': 96,
#     'Eleanor': 86,
#     'Freddie': 91
# }
import random
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# passed_students = {new_key:new_value for (key, value) in dictionary.items()}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 65}
print(f'passed students ${passed_students}')
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
    grade = student_scores[score]
    if grade >= 91 and grade <= 100:
        student_grades[score] = 'Outstanding'
    elif grade >= 81 and grade < 91:
        student_grades[score] = 'Exceeds Expectations'
    elif grade >= 71 and grade < 81:
        student_grades[score] = 'Acceptable'
    elif grade < 70:
        student_grades[score] = 'Fail'
    
print(student_grades)
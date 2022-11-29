import os 
os.system('cls')

grades = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62,}
grade = grades.copy()

for key, value in grade.items():
    if value >= 91:
        grades[key] = 'Outstanding'
    if value <= 90 and value >= 81:
        grades[key] = 'Exceeds Expectations'
    if value <= 80 and value >= 71:
        grades[key] = "Acceptable"
    if value <= 70:
        grades[key] = 'Fail'

print(grades)
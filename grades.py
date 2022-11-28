grades = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62,}
grade = grades.values()

for item in grade:
    if item >= '91':
        grades[item] = "Outstanding"
    elif item <= '90' and item >= '81':
        grades[item] = "Exceeds Expectations"
    elif item <= '80' and item >= '71':
        grades[item] = "Acceptable"
    elif item <= '70':
        grades[item] = 'Fail'
    
    
print(grades)
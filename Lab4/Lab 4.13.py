# Given a list of student grades, calculate the average grade for each student and store them in a dictionary.

grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85], 'Charlie': [90, 91, 89]}
average_grades = {}

for student, grade_list in grades.items():
    average_grades[student] = sum(grade_list) / len(grade_list)

print("Average Grades:", average_grades) #Output: Average Grades: {'Alice': 89.0, 'Bob': 86.66666666666667, 'Charlie': 90.0}
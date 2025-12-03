"""P6. Student Grade Categorization (Dict, If, For)
Create a program that categorizes students based on their grades.

Requirement Specifications:
Use a dictionary student_grades where keys are student names (strings)
 and values are their grades (floats):
{'Alex': 85.5, 'Ben': 92.0, 'Chris': 78.0, 'Dana': 88.5, 'Erin': 95.0}.
Initialize empty lists for each grade category: A, B, C, and D.
Iterate through the student_grades dictionary using a for loop.
For each student, use if/elif/else statements to determine their grade category 
based on the following criteria:
A: 90 and above
B: 80 to 89
C: 70 to 79
D: Below 70
Append each student’s name to the appropriate grade category list.

Output:
Print the students in each grade category.

Concept Focus: dict (creation, iteration over items), if/elif/else (conditional logic), for loop."""

student_grades = {'Alex': 85.5, 'Ben': 92.0, 'Chris': 78.0, 'Dana': 88.5, 'Erin': 95.0}
A, B, C, D = [], [], [], []
for student, grade in student_grades.items():
    if grade >= 90:
        A.append(student)
    elif grade >= 80:
        B.append(student)
    elif grade >= 70:
        C.append(student)
    else:
        D.append(student)

print("Grade A students", A)
print("Grade B students", B)
print("Grade C students", C)
print("Grade D students", D)

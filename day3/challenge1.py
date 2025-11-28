# P1. Event Attendee Management System ( If, For)
# A school is organizing a field trip and needs to manage the list of confirmed student attendees.
# Initial Data: You need to choose an appropriate data structure to store the names of students who have signed up. Options include a list. Briefly justify your choice and create the data structure with the following names: ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona"].
# Requirement Specifications:
# The system should allow the user to input a student name for attendance management.
# The system must check if the entered name exists in the chosen data structure.
# If the name exists, the system should confirm the student's attendance.
# If the name does not exist, the system should notify the user that the student is not on the list.
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona"]
name = input("Enter a student name: ")
for student in students:
    if name == student:
        print(f"Attendance has been marked for {student}")
        break
else:
    print("Student is not on the list.")


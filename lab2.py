# Lab 2: Input/Output Formatting for Structured Data
# Objective:
# Learn how to read user input, convert types, and display data neatly.
# Problem Statement:

# Ask the user to enter first name, last name, and age.
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))

# Ask the user to enter height in meters (float).
height = float(input("Enter height in meters: "))

# Display the data in a structured format using f-strings 
# with two decimal places for height.
print(f"{first_name} {last_name} is {age} years old and {height:.2f} meters tall.")

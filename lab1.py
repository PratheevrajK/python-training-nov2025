### Lab 1: Data Type Conversions
#### Objective:
##### Practice converting between strings, integers, floats, and booleans.
##### Problem Statement:

##### 1.	Ask the user to enter a number (as a string).
str_value = input("Enter any number: ")
print(str_value, type(str_value))

##### 2.	Convert it to integer and float.
int_value = int(str_value)
print(int_value, type(int_value))

float_value = float(str_value)
print(float_value, type(float_value))

##### 3.	Perform a simple arithmetic operation with both.
sum = int_value + float_value
print("Sum of {} and {} is: ".format(int_value, float_value), sum)

##### 4.	Convert a non-empty string to a boolean and print the result.
bool_value = bool(str_value)
print(f"bool_value is {bool_value}")

bool_value2 = bool('')
print(f"bool_value2 is {bool_value2}")
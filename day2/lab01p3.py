# P3. Body Mass Index (BMI) Calculator

weight = float(input("Enter weight in kilograms(kg): "))
height = float(input("Enter height in meters(m): "))

bmi = weight/height**2

print("BMI value: {:.2f}".format(bmi))

# print(f"BMI value: {bmi:.2f}")
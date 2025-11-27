# Lab 3: Length Converter (Meters ↔ Feet)
# Objective:
# Practice type conversion and input/output formatting for a real-world scenario.
# Problem Statement:
METER_TO_FEET = 3.28084

# Ask the user to enter a length in meters.
meter_value = int(input('Enter length in meters: '))

# Convert meters to feet (1 meter = 3.28084 feet).
feet_value = METER_TO_FEET * meter_value

# Display both values formatted to 2 decimal places.
print(f"{meter_value:.2f} meter is {feet_value:.2f} feet")
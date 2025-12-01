# Extract Numbers from a given string
# Example: The apple costs Rs.12 and oranges costs Rs.50
# Ouput: 12, 50
# Example: the apple costs Rs.12.50 and oranges costs Rs.35.45
# Output: 12.50, 35.45

sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    if word[0:3] == "Rs.":
        print(word[3:], end=", ")

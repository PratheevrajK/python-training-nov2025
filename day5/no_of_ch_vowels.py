# Given a string (input from the user)
# print - Number of Characters, number of Words
# Print number of vowels

sentence = input("Enter a sentence: ")

print(f"Number of chars: {len(sentence)}")

words = sentence.split()
print(f"Number of words: {len(words)}")

count = 0
for ch in sentence.lower():
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        count+=1
print(f"Number of vowels: {count}")

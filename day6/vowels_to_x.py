# Replace vowels to 'x' in the given string.
sentence = input("Enter a sentence: ")
input_list = list(sentence)
vowels = 'aeiou'
for i in range(len(input_list)):
    if input_list[i] in vowels:
        input_list[i] = 'x'
output = ''.join(input_list)
print(output)

# Frequency counter for vowels in a given string.
word = input("Enter any string: ")
vowels = "aeiouAEIOU"
freq_counter = {}
for ch in word:
    if ch in vowels:
        freq_counter[ch] = freq_counter.get(ch, 0) + 1
print(freq_counter)

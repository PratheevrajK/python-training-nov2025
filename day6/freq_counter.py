# Frequency counter in a given string.
word = input("Enter any string: ")
freq_counter = {}
for ch in word:
    freq_counter[ch] = freq_counter.get(ch, 0) + 1
print(freq_counter)

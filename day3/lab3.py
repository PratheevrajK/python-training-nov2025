# WAP to count number of vowel in given string
word = input("Enter any word: ")
word = word.lower()
count = 0
cons_count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
    else:
        cons_count += 1
print(f"Total vowels in given word {word} is {count}")
print(f"Total consonants in given word {word} is {cons_count}")

# !user/bin/env/ python
# Author: Pratheevraj K
# Email: pratheevraj002@gmail.com
# Script to find sum and average of 10 numbers taken from user

total = 0
for _ in range(10):
    num = int(input("Enter the number: "))
    total += num

print("The sum of 10 numbers is: ", total)
print("The average of 10 numbers is: ", total/10)
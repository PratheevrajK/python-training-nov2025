# Script to find 2nd highest & 2nd lowest in a list of numbers

# numbers = input("Enter numbers separated by space: ")
# num_list = []
# for i in numbers.split():
#     num_list.append(int(i))
# print(num_list)
num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print(num_list)
num_list.sort()
print("2nd highest number is: ", num_list[-2])
print("2nd lowest number is: ", num_list[1])

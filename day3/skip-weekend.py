#WAP to skip weekends while scheduling a meeting
# 0-Monday, 1-Tuesday,..
for i in range(7):
    if i == 5 or i == 6:
        continue
    print(f"Meeting can be scheduled on {i}")
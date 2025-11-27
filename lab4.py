# WAP to display grade of a student
""" score>=90 then Grade A
    score>=70 then Grade B
    score>=50 then Grade C
    else Grade D
    """

score = int(input("Enter a score: "))

if score>=90:
    print('You have secured Grade A.')
elif score>=70:
    print('You have secured Grade B.')
elif score>=50:
    print('You have secured Grade C.')
else:
    print('You have secured Grade D.')

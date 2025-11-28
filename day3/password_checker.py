#WAP to stop the loop once the correct password is entered. Maximum 3 attempts
correct_password = 'admin123'
for i in range(3):
    password = input("Enter the password: ")
    if password == correct_password:
        print("Successfully logged in!")
        break
    else:
        print(f"Incorrect password - {password}")
if i == 2:
    print("Account has been blocked!")
cycle = 0
while cycle < 3:

    passwords = input("Please Enter The password ")

    if passwords == "pass123":
        print("Access granted")
        break
    else:
        print("Wrong password")
        cycle += 1
print("--------------")
if cycle == 3:
    print("Access denied")
    
    
#   The user is prompted to enter a password.
#   It gives the user only 3 attempts.
#   If the user successfully enters "pass123",
#   it displays "Access granted."
#   If the user has finished trying,
#   it displays "Access denied."
#   (Use while and if)
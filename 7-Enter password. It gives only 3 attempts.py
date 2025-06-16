cycle = 0

while cycle < 3:

    passwords = input("Please Enter The password ")

    if passwords == "pass123":
        print("Access granted")
        break
    else:
        print("Wrong password")
        cycle += 1
print("------------------")
if cycle == 3:
    print("Access denied")
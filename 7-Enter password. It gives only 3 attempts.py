<<<<<<< HEAD
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
=======
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
>>>>>>> d1fcfceaac145ec1d73e0def7f86a83ed7e6263e
    print("Access denied")
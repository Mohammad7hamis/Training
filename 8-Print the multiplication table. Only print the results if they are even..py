number = int(input("Please Enter the number "))

x = "x"
for n in range(1, 5):
    if n*number % 2 == 0 :
        print(number, x, n, "=", number*n)
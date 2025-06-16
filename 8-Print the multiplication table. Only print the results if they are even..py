number = int(input("Please Enter the number "))

x = "x"
for n in range(1, 5):
    if n*number % 2 == 0 :
        print(number, x, n, "=", number*n)


#/ This code will asks the user to enter a number, 
# then uses a for loop to print the multiplication table
# for that number from 1 to 5.
# But only print the results if they are even.
# Don't use (continue) now, only if inside for.
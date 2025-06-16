number = int(input("Enter the Number please! "))
if number > 100:
    print("Too big")
    
elif number >= 50 and number <= 100:
    print("In range")
    
else:
    print("Too small")
#/This code asks the user for a number, then checks:
# If the number is greater than 100, print "Too big"
# If it is between 50 and 100 (inclusive), print "In range"
# If it is less than 50, print "Too small"
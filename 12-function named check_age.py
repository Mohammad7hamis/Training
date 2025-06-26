'''
Write a function called check_age that takes
a number representing age as a parameter. Inside the function:
If the age is under 18, print "You are underage."
If 18 or older, print "You are an adult."
📌 Note: Do not use input inside the function.
'''
def check_age (age):
    if age < 18:
        print("You are underage")
    else:
        print("You are an adult")
        
check_age(21)
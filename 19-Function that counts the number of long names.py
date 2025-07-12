'''
A function that counts the number of long names.
Required:
Ask the user for the number of names.
Receive names using input() within a loop.
Names with 5 or more characters are considered "long."
At the end of the function, print the number of long names.
'''
def count_long_names():

    number_of_names = int(input("Please Enter The number Of Names: "))
    long_name = []

    for n in range (number_of_names):
        names = input(f"Please Enter the number {n+1}: ")
        if len(names) >= 5:
            long_name.append(names)
    return long_name

result = count_long_names()
print("The Number of Long Names Is: ",len(result))
print("The Long Names: ", result)
'''
🔹 Challenge:
Write a program that asks the user to enter 5 names,
and adds to the list only those names that:
Start with a capital letter
Have more than 3 characters
Do not contain numbers
'''
def add():
    number_of_names = int(input("Enter the number of names: "))
    new_names = []
    for n in range (number_of_names):
        
        names = input(f"Please Enter The Name Of Number ({n+1}): ")
        if(
            names[0].isupper()
            and len(names) >= 3
            and names.isalpha
        ):
            new_names.append(names)
    return new_names
result = add()
print(f"The Number of New Name Is : {len(result)} \nAnd The Names Are : {result}")
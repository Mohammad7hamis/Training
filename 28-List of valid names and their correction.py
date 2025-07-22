'''
🎯 Challenge: List and Correct Valid Names
Requirements:
Ask the user for the number of names.
Each name must:
Not be empty after removing spaces
Begin with a capital letter
Do not contain symbols or numbers
Storage only valid names in a list.
'''
num_of_nambers =  int(input("How Many Names? "))
correct_names = []
def Correct_Valid_Names():
    for n in range(num_of_nambers):
        names = input(f"Enter Name ! {n+1} ")
        
        names = names.strip()
        names = names.capitalize()
        if (
            names.isalpha()
        ):
            correct_names.append(names)
    return correct_names
result = Correct_Valid_Names()
print(f"Total Correct Number is : {len(result)} \nAnd The Names are : {result}")
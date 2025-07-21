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
        names = input(f"Enter The Correct Name ! {n+1} ")
        if( names[0].strip
           #and names.capitalize 
           #and names.isalpha
        ):
            correct_names.append(names)
    return correct_names
result = Correct_Valid_Names()
print(result)
#print(f"The Number Of Correct Number is : {len(result)} \nAnd The Names are : {result}")
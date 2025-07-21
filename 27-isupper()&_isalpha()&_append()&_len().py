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
print(f"The Number of new name is : {len(result)} and the names ars : {result}")
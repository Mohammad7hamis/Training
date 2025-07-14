def filtring_names():
    enter_the_name = int(input("Please Enter Number Of Names: "))
    the_name_filter = []
    for n in range(enter_the_name):
        name = input(f"Enter the name {n+1}: ")
        if len(name) >= 5 and (name.startswith('A') or name.startswith('a') and name.endswith('D') or name.endswith('d')):
            the_name_filter.append(name)
    return(the_name_filter)
result = filtring_names()
print("The Number Of Filterd Names is: ",len(result), "\nFilterd Names: ",result)
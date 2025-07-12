'''
Required:
Ask the user how many names to enter.
Receive names using input().
Only store names that:
have 5 or more characters and
begin with the letter "A" or "a"
Print the number of characters + the names themselves.
'''
def filter_names_starting_with_a():
    number_of_names = int(input("Please Enter The number Of Names: "))
    names_begin_a_or_A = []
    
    for n in range(number_of_names):
        names = input(f"Please Enter Name {n+1}: ")
        if len(names) >= 5 and (names.startswith('A') or names.startswith('a')):
            names_begin_a_or_A.append(names)
    return names_begin_a_or_A
result = filter_names_starting_with_a()
print("The Number Of Filtred Name Is ",len(result), "\nAnd Filtred Name is ",result)
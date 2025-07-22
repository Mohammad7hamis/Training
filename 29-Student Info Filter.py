'''
Challenge: Student Info Filter
✅ Requirements:
The user specifies the number of students.
For each student, enter:
Name & Age & City
We verify that:
* The name must contain only letters, with the first letter capitalized.
* The age must be a number between 18 and 25 only.
* The city must be one of: "Riyadh" or "Jeddah" only.
'''
def student_info_filter():
    number_of_student = int(input("How many student do want to add ? "))
    valid_students = {}
    for name, info in number_of_student:
        names = input(f"Please Enter the name {n+1} : ")
        age = int(input(f"Please Enter the age {n+1} : "))
        city = input("Riyadh or Jeddah: ")
        if names.capitalize() and names.isalpha():
            valid_students[names] = age,city
                
        
    return valid_students
result = student_info_filter()
print(result)
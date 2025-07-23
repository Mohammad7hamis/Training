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
def students_info_filter():
    number_of_student = int(input("How many student do want to add? "))
    input_students = {}
    valid_students = {}
    for names in range(number_of_student):
        
        names = input(f"Please Enter the name of student {names+1} : ").strip().capitalize()
        age = (input(f"Please Enter the age of student {names} : "))
        city = input(f"From Which City Is {names}, form ? \nRiyadh or Jeddah : ").strip().capitalize()
        
        if not names.isalpha():
            continue
        
        if not age.isdigit():
            continue
        age = int(age)
        
        if 18 <= age <= 25 and city in ['Riyadh', 'Jeddah']:
            valid_students[names] = {'age': age, 'city': city}
        return valid_students
result = students_info_filter()
for name, info in result.items():
    print(f"Name: {name}, Age: {info['age']}, City: {info['city']}")
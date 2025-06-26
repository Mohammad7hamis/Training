'''
✏️ Write a function called show_grade.
It takes:
grades: A dictionary containing student names and grades.
name: The name of the student whose grade you want to find.
If the name exists:
Print: "Grade for <name> is <grade>"
If it doesn't exist:
Print: "Student not found."
'''
def show_grade(grades, the_names):
    if the_names in grades:
        print("Grade for", the_names, "is", grades[the_names], "." )
    else:
        print("Student not found.")
        
grades = {"Mohammad": 95, "Sara": 88, "Ali": 46, "Hebah": 99}
show_grade(grades,"Hebah")
show_grade(grades,"Huda")
'''
✅ Requirements:
The grade must be 80 or higher. ✅
The job description must be "Student" or "student." ✅
Save the results in a dictionary under the name top_students.
Print the number of successful students, their names, and their grades.
'''
def filter_top_students():
    top_students = {}
    students_info = {
        "Mohammad": (95, "Student"),
        "Ali": (81, "student"),
        "Sara": (78, "Student"),
        "Huda": (66, "emloyee"),
        "Nora": (88, "Student"),
        "Zaid": (48, "sudent")
    }
    for name, (grade, description) in students_info.items():
        if (grade >= 80) and (description.lower() == "student" ):
            top_students[name] = (grade, description)
            
    return top_students
result = filter_top_students()
print("Top Students: (",len(result),")")
for name, (grade, descrption) in result.items():
    print(name,":", grade)
'''
Write a function called filter_passed_students.
Use a dictionary containing student names and their grades.
Extract only students with a grade of 50 or higher.
Return a new dictionary containing only those who passed.
Print the number of students who passed, their names, and their grades.
'''
def filter_passed_students():
    passd_student = {}
    student_name = {"Mohammad": 95,
                    "Ali": 42,
                    "Sara": 78,
                    "Huda": 30 
                    }
    for name, grade in student_name.items():
        if grade >= 50:
            passd_student[name] = grade
    return passd_student
result = filter_passed_students()
print("Passed Students (",len(result), "):")
for name, grade in result.items():
    print(name, ":", grade)
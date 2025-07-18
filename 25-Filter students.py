'''
🎯 Challenge: Filter students according to the following conditions:
✅ Required:
Write a function that returns only students who:
Have a grade of 80 or higher
Have a job title of "Student"
And are aged 21 or older
'''
def filtering_student_info():
    filter_of_student = {}
    students = {
        "Mohammad": {"grade": 95, "job": "Student", "age": 21},
        "Ali": {"grade": 81, "job": "Sudent", "age": 19},
        "Sara": {"grade": 78, "job": "Employee", "age": 25},
        "Huda": {"grade": 66, "job": "Student", "age": 23},
        "Zaid": {"grade": 88, "job": "Student", "age": 23}
    }
    for name, info in students.items():
        if (info["grade"] >= 80) and (info["job"].lower() == "student") and (info["age"] >= 21):
            filter_of_student[name] = info
    
    return filter_of_student
result = filtering_student_info()
print("\nFiltered Students:\n")
for name, info in result.items():
    print("Name:", name)
    print("Grade:", info["grade"])
    print("Job:", info["job"])
    print("Age:", info["age"])
    print("-" * 20)

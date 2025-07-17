'''
Filter students by grade and job title
Required:
You have a dictionary containing student names as keys.
Each student has information stored within a tuple containing:
Their grade (int)
Their job title or attribute (str), such as "student", "employee"
Write a function called filter_students_info().
This function will extract only students who:
Have a grade of 50 or higher ✅
Have a description of "student" only ✅
Return a dictionary containing only successful students.
'''
def filter_sudents_inf():
    passed_student = {}
    student_info = {
                    "Mohammad":(95, "Student"),
                     "Ali": (42, "Student"),
                     "Sara": (78, "employee"),
                     "Huda": (66, "Student"),
                     "Zaid": (48, "Sudent") 
    }
    for name, (grade, description) in student_info.items():
        if grade >= 50 and description == "Student":
            passed_student[name] = (grade, description)
    return passed_student
result = filter_sudents_inf()
print("Passed Students: (",len(result), ")")
for name, (grade, description) in result.items():
    print(name,":", grade)
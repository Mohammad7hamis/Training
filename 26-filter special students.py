'''
🎯 Challenge: Filter Outstanding Students
We have a database containing students and their information
(grade, profession, age, city).
We want to extract students who:
Have a grade of 85 or higher
Among the professions is "student" only
Are between 20 and 25 years old (inclusive)
Reside in Riyadh or Jeddah only
'''
def filter_special_students():
    special_students = {}
    students = {
    "Mohammad": {"grade": 95, "job": "Student", "age": 21, "city": "Riyadh"},
    "Ali": {"grade": 81, "job": "Student", "age": 22, "city": "Dammam"},
    "Sara": {"grade": 89, "job": "student", "age": 24, "city": "Jeddah"},
    "Huda": {"grade": 90, "job": "employee", "age": 23, "city": "Riyadh"},
    "Zaid": {"grade": 87, "job": "Student", "age": 19, "city": "Jeddah"},
    "Lama": {"grade": 91, "job": "Student", "age": 22, "city": "Makkah"}
}
    for name, info in students.items():
        if (
          info['grade'] >= 85
          and info ['job'].lower() == 'student'
          and 20 <= info['age'] <= 25 
          and info['city'].lower() in ['riyadh','jeddah']
        ):
            special_students[name] = info
    return special_students
result = filter_special_students()
print(f"Number of special student: ({len(result)})")
print("-"*15)
for name, info in result.items():
    print(f"Name: {name}.\nGrade: {info['grade']}.\nAge: {info['age']}.\nCity: {info['city']}.")
    print("-"*15)
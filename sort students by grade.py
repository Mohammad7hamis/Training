'''
🧠 Challenge: Sort students by grade
📌 Requirements:
Write a function called sort_students_by_grade()
that takes a dictionary containing student data (name, grade),
and returns a list sorted in descending order by grade.
'''
def sort_students_by_grade():
    sort_students = {}
    students = {
        "Mohammad": 95,
        "Ali": 81,
        "Sara": 89,
        "Huda": 90,
        "Zaid": 87,
        "Lama": 91
    }
    sort_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    return sort_students
result = sort_students_by_grade()
print(result)
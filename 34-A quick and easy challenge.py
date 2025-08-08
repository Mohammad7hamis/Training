def analyze_students():
    students = {
        "Ali": {'grade': 90, 'city': 'Riyadh'},
        "Sara": {'grade': 85, 'city': 'Jeddah'},
        "Mohammad": {'grade': 100, 'city': 'Makkah'},
        "Khalid": {'grade': 70, 'city': 'Jeddah'},
        "Nabli": {'grade': 89, 'city': 'Riyadh'},
        "Ahmed": {'grade': 98, 'city': 'Jeddah'}
}
    return students
result = analyze_students()

if result:
    grades = [info['grade'] for info in result.values()]
    
    average_grades = sum(grades) / len(grades)
    max_grades = max(grades)
    top_student = [name for name, info in result.items() if info['grade'] == max_grades][0]
    
    print(f"Average Grade: {average_grades:.2f}")
    print(f"Top Grade: {max_grades}")
    print(f"Top student: {top_student}")
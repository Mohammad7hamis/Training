def ideal_student_01():
    input_number = int(input("How many student do want to add ? "))
    Sorted_Students = {}
    for name in range(input_number):
        input_name = input(f"Enter the name of student number ({name+1}) ").strip().capitalize()
        input_grade = input(f"Enter the grade of {input_name}: ").strip()
        input_city = input(f"Enter the city of {input_name}: " ).strip().title()
        input_job = input(f"Enter the job of {input_name}: ").strip().lower()
        input_age = input(f"Enter the age of {input_name}: ").strip()
        
        if not input_name.isalpha():
            continue
        if not input_grade.isdigit():
            continue
        input_grade = int(input_grade)
        if not input_age.isdigit():
            continue
        input_age = int(input_age)
        if( input_grade >= 70
          and input_city in ["Jeddah","Riyadh"]
          and input_job.lower() == "student" 
          and 18 <= input_age <= 25
        ):
            Sorted_Students = dict(sorted(Sorted_Students.items(), key=lambda x: x[1], reverse=True))
            Sorted_Students[input_name] = {'grade': input_grade, 'city': input_city, 'age': input_age,}
    return Sorted_Students
result = ideal_student_01()
print(f"📚 Sorted Students by Grade (High to Low): 📚 ({len(result)})\n")
print("----  🔍 Sorted Students 🔎  ----")
for name, info in result.items():
    print(f"Name: {name}.\nGrade: {info['grade']}.\nCity: {info['city']}\nAge: {info['age']}")
    print("-"*31)
print("--- 🔍 Sorted Students End 🔎 ---")
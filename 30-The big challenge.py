def ideal_student_00():
    number_of_student = int(input("How many student do you want to add ? "))
    accepted_student = {}
    for name in range(number_of_student):
        input_student = input(f"Enter the name of student ({name+1}) ").strip().capitalize()
        input_grade = input(f"Enter the grade of student {input_student}: ").strip()
        input_jop = input(f"Enter {input_student} jop: ").strip().lower()
        input_city = input(f"Enter {input_student} city: ").strip().title()
        input_age = input(f"Enter {input_student} age: ").strip()
        
        if not input_student.isalpha():
            continue
        if not input_grade.isdigit():
            continue
        input_grade = int(input_grade)
        if not input_age.isdigit():
            continue
        input_age = int(input_age)
        if( input_grade >= 85 
           and input_jop.lower() == 'student'
           and input_city in ['Jeddah','Riyadh']
           and 20 <= input_age <= 25
        ):
            accepted_student[input_student] = {'grade':input_grade, 'city':input_city, 'age':input_age}
    return accepted_student
result = ideal_student_00()
print(f"📌 Number of accept stuednts 📌 ({len(result)})\n")
print("----  🔍 Accept Students 🔎  ----")
for name,info in result.items():
    print(f"Name: {name}.\nGrade: {info['grade']}.\nCity: {info['city']}\nAge: {info['age']}")
    print("-"*31)
print("--- 🔍 Accept Students End 🔎 ---")
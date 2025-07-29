def ideal_student_02():
    enter_number = int(input("How Many Student Do You Want To Add ? "))
    sorted_student = {}
    for name in range(enter_number):
        enter_name = input(f"Enter The Name Of Student ({name+1}): ").strip().capitalize()
        enter_grade = input(f"Enter The Grade Of {enter_name}: ").strip()
        enter_city = input(f"Enter The City Of {enter_name}: ").strip().title()
        enter_job = input(f"Enter The Job Of {enter_name}: ").strip()
        enter_age = input(f"Enter The Age Of {enter_name}: ").strip()
        
        if not enter_name.isalpha():
            continue
        if not enter_grade.isdigit():
            continue
        enter_grade = int(enter_grade)
        if not enter_age.isdigit():
            continue
        enter_age = int(enter_age)
        if( enter_grade >= 70
           and enter_city in ["Jeddah", "Riyadh"]
           and enter_job.lower() == "student"
           and 18 <= enter_age <= 25
        ):
            sorted_student[enter_name] = {
                'grade': enter_grade,
                'city': enter_city,
                'age': enter_age
            }
            
    sorted_student = dict(sorted(sorted_student.items(), key=lambda value:value[1]['grade'], reverse=True))
    return sorted_student
result = ideal_student_02()
print(f"📥Sorted Students by Grade (High to Low): ({len(result)})📤\n")
print("-----  🔍 Sorted Students 🔎  -----")
for name, info in result.items():
    print(f"Name: {name}.\nGrade: {info['grade']}.\nCity: {info['city']}.\nAge: {info['age']}")
    print("-"*31)
print("-- 🔍 Sorted Students End 🔎 --")
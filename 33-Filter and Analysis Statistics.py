def ideal_student_02():
    enter_number = int(input("How Many Student Do You Want To Add ? "))
    sorted_student = {}
    for name in range(enter_number):
        enter_name = input(f"Enter The Name Of Student ({name+1}): ").strip().capitalize()
        enter_gender = input(f"Enter The Gender of {enter_name}: ").strip().capitalize()
        enter_grade = input(f"Enter The Grade Of {enter_name}: ").strip()
        enter_city = input(f"Enter The City Of {enter_name}: ").strip().title()
        enter_job = input(f"Enter The Job Of {enter_name}: ").strip()
        enter_age = input(f"Enter The Age Of {enter_name}: ").strip()
        # التأكد من صحة البيانات
        if(
           not enter_name.isalpha() 
           or not enter_gender.isalpha()
           or not enter_grade.isdigit()
           or not enter_age.isdigit() 
        ):
            continue
        # تحويل المدخلات إلى أرقام صحيحة
        enter_grade = int(enter_grade)
        enter_age = int(enter_age)
        # الشروط
        if( enter_grade >= 75
           and enter_gender.lower() == "male"
           and enter_city in ["Jeddah", "Riyadh"]
           and enter_job.lower() == "student"
           and 18 <= enter_age <= 25
        ):
            # تحديث / تخزين البيانات داخل القاموس
            sorted_student[enter_name] = {
                'gender': enter_gender,
                'grade': enter_grade,
                'city': enter_city,
                'age': enter_age
            }
    return sorted_student
result = ideal_student_02()

if result:
    # إنشاء قائمة جديدة تحتوي جميع الدرجات
    grades = [info['grade'] for info in result.values()]
    # العمليات الحسابية
    averge_grades = sum(grades) / len(grades)
    max_grades = max(grades)
    
    print(f"📥 Number of accepted students: ({len(result)})📤\n")
    print(f"📈 Average grades: {averge_grades:.2f}📈")# رقمين فقط بعد الفاصلة العشرية
    print(f"🏆 Hightst grade: {max_grades} 🏆")
    print("-----  📬 Accepted Students Info 📬  -----")
for name, info in result.items():
    print(f"Name: {name}.\nGender: {info['gender']}.\nGrade: {info['grade']}.\nCity: {info['city']}.\nAge: {info['age']}")
    print("-"*31)
else:
    print("📭 No accepted students 📭")

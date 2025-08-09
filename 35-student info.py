def student_info(name, acdemic_stage, number_of_subject, *name_of_academic_subject):
    
    
    print(f"Hello Student: {name}")
    print(f"Level: {acdemic_stage}")
    print(f"Subjects count: {number_of_subject}")
    
    if name_of_academic_subject:
        print("Subject: ", ", ".join(name_of_academic_subject))
        

student_info("Ali", "Secondary", 6, "Math", "Physics", "Chemistry")
def student_info(name, academic_stage, number_of_subject=5, *subjects):
    
    
    print(f"Hello Student: {name}")
    print(f"Level: {academic_stage}")
    print(f"Subjects count: {number_of_subject}")
    
    if subjects:
        print("Subject: ", ", ".join(subjects))
        

student_info("Ali", "Secondary", 6, "Math", "Physics", "Chemistry")
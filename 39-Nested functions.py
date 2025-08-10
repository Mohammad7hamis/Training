def calculate_grade(*name_and_grades):
    print(f"Student: {name_and_grades[0]}")
    global average
    def average():
        numbers = name_and_grades[1:]
        return sum(numbers) / len(numbers)
    result = average()
       

    def result():
        if result >= 50:
            print("Student: Passed")
        else:
            print("Student: Faild")
    result()
        
calculate_grade("Ali", 70, 65, 80, 90)
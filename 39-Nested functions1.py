def calculate_grade(*name_and_grades):
    print(f"Student: {name_and_grades[0]}") #print just the name

    def average():
        numbers = name_and_grades[1:] #save the just the numbers in the tuple.
        return sum(numbers) / len(numbers)
    the_average = average()
    print(f"Average: {the_average}")
    

    def result():
        if the_average >= 50:
            print("Result: Passed")
        else:
            print("Result: Failed")
    result()   
calculate_grade("Ali", 70, 65, 80, 90)
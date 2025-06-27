''''
✏️ Write a function called show_employee_info
that takes a single tuple containing three elements:

$ Employee Name
$ Job Title
$ Salary
'''
def show_employee_info(employee):
    print("Name: ", employee[0])
    print("Position: ", employee[1])
    print("Salary", employee[2])
# القيمة لا تتغير مع الـ Tuples
employee = ("Ali", "Developer", 7000)
show_employee_info(employee)
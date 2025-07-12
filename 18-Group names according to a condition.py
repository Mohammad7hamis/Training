'''
✏️ Write a function called (collect_short_names):
that does the following:
It asks the user to enter a number of names (for example, 3 names).
It then asks the user to enter each name.
It stores only names with fewer than 5 characters in a list.
It returns this list (using return).
'''
def collect_short_names():
   number_of_student = int(input("How many names? "))
   short_names = []
   for n in range (number_of_student):
       name = input(f"Enter the number {n+1}: ")
       if len(name) < 5:
           short_names.append(name)
   return short_names   
result = collect_short_names()
print("Short names", result)
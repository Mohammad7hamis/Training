'''
✏️ Write a function called search_name.
It takes a list of names
and one name you want to search for.
If the name is in the list,
→ print "Found!"
Otherwise,
→ print "Not found."
'''
def search_name(names,target):
    if target in names:
        print("Found!")
    else:
            print("Not found.")
            
names = ["Ali", "Mohammed", "Sara", "Huda"]
search_name(names, "Mohammed")
search_name(names, "Zaid")
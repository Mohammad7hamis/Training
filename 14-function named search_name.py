def search_name(names,target):
    if target in names:
        print("Found!")
    else:
            print("Not found.")
            
names = ["Ali", "Mohammed", "Sara", "Huda"]
search_name(names, "Mohammed")
search_name(names, "Zaid")
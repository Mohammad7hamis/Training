largest = None
smallest = None

for i in range(5):
    number = int(input("Enter a number: "))

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

print("Largest number is:", largest)
print("Smallest number is:", smallest)

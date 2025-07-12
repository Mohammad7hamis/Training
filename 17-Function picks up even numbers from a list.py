'''
✏️ Write a function called filter_even_numbers.
Get a list of even numbers.
Inside the function:
Use a loop to iterate over the list.
Check if the number is even.
Store only even numbers in a new list.
Finally, return the new list using return.
'''
def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
           even_numbers.append(num)
    return even_numbers
numbers = [3, 8, 10, 5, 80, 6]                      
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)
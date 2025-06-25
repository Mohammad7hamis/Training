'''
Write a function called print_even_numbers that takes
a list of numbers as a parameter and prints
only the even numbers within it.
'''
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)
numbers = [2, 7, 10, 5, 8]
print_even_numbers(numbers)
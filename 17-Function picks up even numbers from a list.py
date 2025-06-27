def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
           even_numbers.append(num)
    return even_numbers
            
numbers = [3, 8, 10, 5, 6]           
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)
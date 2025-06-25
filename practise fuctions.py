# تعريف دالة
def print_numbers1():
    for i in range(-1):
        print(i)
# إدخال المدخل في استدعاء الدالة       
def prtint_numbers2(to):
    for il in range(to):
        print(il)
# تمرير أكثر من مدخل للدالة
def add(st, nd):
    print(st + nd)
# إرجاع قيمة الدالة 1
def multi(n1, n2):
    result = n1*n2
    return result
# إرجاع فيمة الدالة 2
def div(num1, num2):
    return num1//num2
# difference between (print) & (return)
def square_print(numm1):
    the_value = numm1*numm1
    print(the_value)
    
def square_return(numm2):
    return numm2*numm2
# difference between (parameter) & (*parameter)
def sum_list(numbers01):
    total = 0
    for n in numbers01:
        total += n 
    print("Sum: ", total)

def sum_args(*numbers02):
    total_1 = 0 
    for s in numbers02:
        total_1 += s
    print("Sum: ", total_1)  
         
print_numbers1()
prtint_numbers2(11)
add(1, 10)
# إرجاع قيمة الدالة 1
value = multi(2,6)
print(value)
# إرجاع قيمة الدالة 2
res = div(13,1)
print(res)
# تمرير مخرجات دالة إلى أخرى
prtint_numbers2(res)
# difference between (print) & (return)
square_print(5)
the__value = square_return(5)
print(the__value)

sum_list([3, 5, 7])
sum_args(3, 5, 7)
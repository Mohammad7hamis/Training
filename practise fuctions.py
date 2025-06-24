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

print_numbers1()
prtint_numbers2(11)
add(1, 10)
# إرجاع قيمة الدالة 1
value = multi(2,6)
print(value)
# إرجاع قيمة الدالة 2
res = div(13,1)
print(res)
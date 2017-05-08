# task_ 1. (a + b * c)2
#       2. a - 4 * b / c
#       3. (a * b + 4) / (c - 1)
'''
a = 2
b = 7
c = 9
result1 = (a + b * c)**2
result2 = a - 4 * b / c
result3 = (a * b + 4) / (c - 1)
print("Результат первого уравнения =", result1)
print("Результат второго уравнения =  %.2f" % result2)
print("Результат тертьего уравнения =", result3)
'''

# task_4 Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

"""
def multiply(number):
    str_number = str(number)
    lst_number = list(str_number)
    mult = 1
    for i in lst_number:
        i = int(i)
        if i % 2 != 0:
            mult *= i
    print(mult)
str_number = str(number)
lst_number = list(str_number)
multiply = 1
for i in lst_number:
    i = int(i)
    if i % 2 != 0:
        multiply *= i
"""

def multiply(number):
    str_number = str(number)
    lst_number = list(str_number)
    mult = 1
    for i in lst_number:
        i = int(i)
        if i % 2 != 0:
            mult *= i
    return mult


while True:
    number = input("Введите пятизначное число: ")
    if number.isdigit():
        if 4 > len(number) or len(number) > 6:
            print("Вы ввели не пятизначное число, попробуйте еще раз")
            continue
        else:
            print(multiply(number))
            break
    else:
        print("Вы ввели не цифры, попробуйте еще раз")
        continue
multiply(number)

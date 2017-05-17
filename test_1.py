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
"""
"""
# task 5 Создать программу, выводящую на экран ближайшее к 10 из
# двух чисел, введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.

def nearest_number(main_num, first_num, second_num):
    if abs(main_num - first_num) < abs(main_num - second_num):
        print("Ближайшее число к основному - ", first_num)
    else:
        print("Ближайшее число к основному - ", second_num)
nearest_number(10, 8.5, 11.45)

# task 6 Создать массив из 10 элементов и проинициализировать его простыми числами в случайном порядке

import math
import random

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
lst = []
for a in range(2, 101):
    if is_prime(a):
        lst.append(a)
lst1 = []
b = 0
for i in range(10):
    a = random.randint(i, len(lst)-1)
    b = lst[i]
    lst[i] = lst[a]
    lst[a] = b
    # random.shuffle(lst)
    lst1.append(lst[i])
lst = lst1
print(lst)

# task 7 Найти сумму десяти первых чисел ряда Фибоначчи.

summ = 0
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return (fib(n-1)) + (fib(n-2))

for i in range(1, 11):
    summ += fib(i)
print(summ)

# task 8 В одномерном массиве поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.

import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 10))
min_elem = lst.index(min(lst))
max_elem = lst.index(max(lst))
print(lst)
replace = lst[max_elem]
lst[max_elem] = lst[min_elem]
lst[min_elem] = replace
print(lst)


# task 9 Нормировать одномерный массив случайных чисел. Нормирование означает приведение всех
# значений массива к интервалу [-1;1], причем максимальное абсолютное значение элементов
# после нормирование должно быть равно 1. Например, последовательность {-5, 3, 4}
# после нормирование будет выглядеть {-1, 0.6, 0.8}

lst = [-5, 3, 4]
# max_value = abs(max(lst)-0)
# min_value = abs(min(lst)-0)
# if max_value > min_value:
#     val_max = max_value
# else:
#     val_max = min_value
max_value = abs(max(lst))
min_value = abs(min(lst))
val_max=max(min_value, max_value)

for i in range(len(lst)):
    lst[i] = (lst[i] / val_max)
print(lst)

# task 12 Для проверки остаточных знаний учеников после летних каникул, учитель младших классов
# решил начинать каждый урок с того, чтобы задавать каждому ученику пример из таблицы умножения,
# но в классе 15 человек, а примеры среди них не должны повторяться. В помощь учителю напишите
# программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения
# (от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты). При этом среди
# 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2
# и им подобные пары считать повторяющимися)


import random

lst = list(range(2, 10))
lst1 = list(range(2, 10))
new_lst = []
for i in range(len(lst)):
    for j in range(len(lst1)):
        mult_pair = "%s*%s" % (lst[i], lst1[j])
        if mult_pair in new_lst or mult_pair[::-1] in new_lst:
            continue
        else:
            new_lst.append(mult_pair)

final_lst = list(set(new_lst))[:15]
random.shuffle(final_lst)
print(final_lst)
"""

# task 10 Вывести на экран матрицу, транспонированную заданной (3*8)

def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end="\t")
        print()

table = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [7, 5, 2, 1, 3, 7, 5, 4]
    ]
new_table = [[0 for z in range(len(table))] for x in range(len(table[0]))]

print_table(table)
print()

for i in range(len(table)):
    for j in range(len(table[i])):
        new_table[j][i] = table[i][j]
print_table(new_table)

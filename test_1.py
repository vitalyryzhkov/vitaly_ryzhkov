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
"""
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

"""
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
"""
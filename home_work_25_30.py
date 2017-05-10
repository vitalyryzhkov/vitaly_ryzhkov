# planets = [' mercury', ' mars', ' earth', ' venus']
#
# def normalize_name_of_planets(planets):
#     for i, elem in enumerate(planets):
#         planets[i] = i[1:]
#     print(planets)
#
# normalize_name_of_planets(planets)

# task_25

# lst = [1, 1, 1, 1, 1]
# def avr_lst(lst):
#     sum_list_elem = 0
#     for i in lst:
#         sum_list_elem += i
#     print(sum_list_elem/len(lst))
# avr_lst(lst)

# task_26

# lst = [1, 2, 4, 5, 7, 8, 9]
#
# def difference_even_odd(lst):
#     sum_odd = 0
#     sum_even = 0
#     for i in lst:
#         if i % 2 != 0:
#             odd = i
#             sum_odd += odd
#         else:
#             even = i
#             sum_even += even
#
#     print(abs(sum_odd - sum_even))
# difference_even_odd(lst)

# task_27

# import random
# lst = []
# lst1 = []
# for i in range(100):
#     if i % 2 != 0:
#         lst.append(i)
# print(lst)
# b = 0
# for i in range(len(lst)-1):
#     a = random.randint(i, len(lst)-1)
#     b = lst[a]
#     lst[a] = lst[i]
#     lst[i] = b
# print(lst)
# task_28

# import random
# lst1 = []
# lst2 = []
# sum_lst1 = 0
# sum_lst2 = 0
# for i in range(5):
#     lst1.append(random.randint(0, 6))
#     lst2.append(random.randint(0, 6))
# for a in lst1:
#     sum_lst1 += a
# for c in lst2:
#     sum_lst2 += c
#
# avr_sum_lst1 = sum_lst1/len(lst1)
# avr_sum_lst2 = sum_lst2/len(lst2)

# def create_list(num, lower_limit, upper_limit):
#     create_lst = []
#     for i in range(num):
#         create_lst.append(random.randint(lower_limit, upper_limit))
#     return create_lst
#
# def sum_list(lst):
#     sum_lst = 0
#     for i in lst:
#         sum_lst += i
#     return sum_lst
#
# lst1 = create_list(5, 0, 5)
# lst2 = create_list(5, 0, 5)
# sum_lst1 = sum_list(lst1)
# sum_lst2 = sum_list(lst2)
# avr_lst1 = sum_lst1/len(lst1)
# avr_lst2 = sum_lst2/len(lst2)
#
# print(lst1)
# print(lst2)
# if avr_lst1 > avr_lst2:
#     print("Среднее арифметическое первого списка больше")
# elif avr_lst1 < avr_lst2:
#     print("Среднее арифметическое второго списка больше")
# else:
#     print("Средние арифметические списков равны")
#
# print(sum_lst1, avr_lst1)
# print(sum_lst2, avr_lst2)
# print(lst2, sum_lst2, avr_sum_lst2)

# task_29

# lst = []
# for i in range(11):
#     lst.append(random.randint(-1, 1))
# a = lst.count(1)
# b = lst.count(0)
# c = lst.count(-1)
# d = 0
# def a2b2c(a, b, c):
    # print(a, b, c)
    # if a == b or b == c or c == a:
    #     return
    # if a > b and a > c:
    #     d = 1
    # elif b > a and b > c:
    #     d = 0
    # elif c > a and c > b:
    #     d = -1
    # print(lst)
    # print("Чаще всего встречается:", d)
# a2b2c(a, b, c)
# task_30

import string

input_string = input("Введите строку для шифрования: ")
lst_password = []

def encryption(input_string):
    encryption_table = string.printable + "йцукенгшщзхъЙЦУКЕНГШЩЗХЪфывапролджэФЫВАПРОЛДЖЭячсмитьбюЯЧСМИТЬБЮ"
    lst_encryption_table = list(encryption_table)
    for i in range(len(input_string)):
        find_idx = encryption_table.find(input_string[i])
        new_index = find_idx + 5
        if new_index > len(encryption_table):
            new_index = (find_idx + 5)%len(encryption_table)
        lst_password.append(lst_encryption_table[new_index])
    password = ''.join(lst_password)
    return password
print(encryption(input_string))

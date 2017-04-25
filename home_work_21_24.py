# import random
#
# def avr_random_numbers(num_randoms, lower_limit, upper_limit):
#     avr_num = 0
#     for i in range(num_randoms):
#         num = random.randint(lower_limit, upper_limit)
#         # print(num)
#         avr_num = avr_num + num
#     print("Среднее арифметическое =", avr_num/num_randoms)
#
# avr_random_numbers(10, 0, 10)

# task_21
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

for a in range(1, 101):
    if is_prime(a):
        print(a)

# task_22

# import random
#
# def random_twelve_num(lower_limit, upper_limit):
#     num = random.randint(lower_limit, upper_limit)
#     print("Рандомное двенадцатизначное число =", num)
#     print("Двенадцатизначное число, разложенное на цифры:")
#     max_num = 0
#     for i in str(num):
#         i = int(i)
#         if max_num < i:
#             max_num = i
#         print(i)
#     print("Максимальное из разложенных цифр =", max_num)
#
#
# random_twelve_num(int(1e11), int(1e12-1))

# task_23

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

# task_24

# import random
#
# def find_number():
#     print("Для завершения, введите '111'")
#     prog_num = random.randint(0, 10)
#
#     while True:
#         num = int(input("Введите числов от 0 до 10:"))
#         if num == 111:
#             break
#
#         if num < 0 or num > 10:
#             print("Вы ввели неверное число, прочитайте условие!")
#             continue
#
#         if num < prog_num:
#             print("Больше")
#
#         elif num > prog_num:
#             print("Меньше")
#
#         elif num == prog_num:
#             print("Угадал")
#             break
#
# find_number()

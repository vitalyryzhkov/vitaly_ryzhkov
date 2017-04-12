# task_14

# def is_even(number):
#     result = number % 2
#     if result == 0:
#         result = "Число является четным"
#     else:
#         result = "Число является нечетным"
#     return result
#
# print(is_even(int(input("Введите число:"))))


# task_15

# task_16

# task_17
from math import *

def is_quadratic(a, b, c):
    diskr = pow(b, 2) - 4 * a * c
    if diskr > 0:
        x1 = (-b-sqrt(diskr))/(2*a)
        x2 = (-b+sqrt(diskr))/(2*a)
    elif diskr == 0:
        x1 = x2 = (-b)/(2*a)
    elif diskr < 0:
        x1 = x2 = "none"
    return x1, x2

a = int(input("Введите первый коэффициент квадратоного уравнения: "))
b = int(input("Введите второй коэффициент квадратоного уравнения: "))
c = int(input("Введите свободный член квадратоного уравнения: "))
print("Результат вычисления квадратного уравнения при a = %d, b = %d и c = %d равен: "
      % (a, b, c), is_quadratic(a, b, c))


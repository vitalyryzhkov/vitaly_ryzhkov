# task_14
"""
def is_even(number):
    result = number % 2
    return result == 0
    # if result == 0:
    #     return True
    # else:
    #     return False
# print(type(is_even(5)))
print("Number is even?:", is_even(int(input("Enter any number: "))))
"""

# task_15
from math import *

x1 = 1
x2 = 2
y1 = 8
y2 = 14
r1 = 4
r2 = 7

def circles_intersect():
    distance_between_centers = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    result = distance_between_centers - (r1+r2)
    if result >= 0:
        print("Circles is intersect")
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("Circles are the same")
    else:
        print("Circles do not intersect")
        return result

circles_intersect()

# task_16

# task_17
"""
from math import *

def solve_quadratic_equation(a, b, c):
    diskr = pow(b, 2) - 4 * a * c
    if diskr > 0:
        x1 = (-b-sqrt(diskr))/(2*a)
        x2 = (-b+sqrt(diskr))/(2*a)
    elif diskr == 0:
        x1 = x2 = (-b)/(2*a)
    elif diskr < 0:
        x1 = x2 = None
    return x1, x2

a = int(input("Введите первый коэффициент квадратоного уравнения: "))
b = int(input("Введите второй коэффициент квадратоного уравнения: "))
c = int(input("Введите свободный член квадратоного уравнения: "))
print("Результат вычисления квадратного уравнения при a = %d, b = %d и c = %d равен: "
      % (a, b, c), solve_quadratic_equation(a, b, c))
"""

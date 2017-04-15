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
x2 = 8
y1 = 2
y2 = 7
r1 = 1
r2 = 1

def is_circles_intersect():
    distance_between_radii = sqrt(pow((x2-x1), 2)+pow((y2-y1), 2))
    if distance_between_radii <= (r1+r2):
        print("Circles is intersect")
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("Окружности одинаковы")
    else:
        print("Окружности не пересекаются")
        return distance_between_radii

is_circles_intersect()

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

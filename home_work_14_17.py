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
r1 = 7
r2 = 3

def is_circles_intersect():
    distance_between_centers = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    if distance_between_centers > r1 + r2 and distance_between_centers < (r1 - r2):
        return False
    elif distance_between_centers == (r1 - r2) or (r1 + r2):
        return True
    elif distance_between_centers > (r1 - r2) and distance_between_centers < (r1 + r2):
        return True
print("Is circles intersect?:", is_circles_intersect())

# task_16
def train_collision_results(first_train_speed, second_train_speed):
    first_train_time = 4 / first_train_speed
    second_train_time = 6 / second_train_speed
    if first_train_time > second_train_time:
        return True
    else:
        return False
print("Is trains are collision?:", train_collision_results(50, 70))

first_train_speed = 50
second_train_speed = 70
first_train_time = 4 / first_train_speed
second_train_time = 6 / second_train_speed

if first_train_time < second_train_time:
    print("Поезда не столкнутся")
else:
    print("Поезда столкнутся")

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

import math
def print_line(line="="):
    print(line*100)

def print_star(star="*"):
    print(star*7)
# task_11
print_star()
print("Task #11: Перевод градусов в радианы")
print_line()

def degrees2radians(deg1=60, deg2=45, deg3=40):
    result_deg1 = math.radians(deg1)
    result_deg2 = math.radians(deg2)
    result_deg3 = math.radians(deg3)
    return result_deg1, result_deg2, result_deg3

print("Результат перевода градусов в радианы = ", degrees2radians())

print_line()

print_star()
print("Task#11_2: Перевод градусов в радианы, вариант №2")
print_line()

def degre2rad(deg):
    return deg * math.pi / 180

print("Результат перевода 60 градусов в радианы =", degre2rad(60))
print("Результат перевода 45 градусов в радианы =", degre2rad(45))
print("Результат перевода 40 градусов в радианы =", degre2rad(40))

print_line()
print_star()
print("Task#12: Сумма трех чисел")
print_line()
# task_12

def find_sum(any_number=int(input("Enter any number: "))):
    number1 = any_number % 10
    number2 = any_number // 10 % 10
    number3 = any_number // 100
    return number1 + number2 + number3

print("The result of your equation is:",  find_sum())

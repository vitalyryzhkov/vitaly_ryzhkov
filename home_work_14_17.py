def is_even(number):
    result = number % 2
    if result == 0:
        result = "Число является четным"
    else:
        result = "Число является нечетным"
    return result

print(is_even(int(input("Введите число:"))))

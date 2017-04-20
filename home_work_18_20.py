# task_19

sum_of_all_numbers = 0
for x in range(1000000):
    x = x**3
    if x % 3 == 0:
        sum_of_all_numbers = sum_of_all_numbers + x
print("Сумма всех чисел от 0 до 1000000 равна:", sum_of_all_numbers)


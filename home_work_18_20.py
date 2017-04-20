# task_19

sum_of_all_numbers = 0
for x in range(1000000):
    x = x**3
    if x > 0 and x <= 1000000:
        sum_of_all_numbers = sum_of_all_numbers + x
print("Сумма всех чисел, которые являются степенью 3ки от 0 до 1000000 равна:", sum_of_all_numbers)

# task_20

for x in range(1000):
     if '1' in str(x) and '7' in str(x):
            print(x)

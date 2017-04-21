# task_18

first_sym = ord('a')
second_sym = ord('c')
for i in range(first_sym, second_sym):
    idx_sum = first_sym + second_sym
    first_sym = first_sym + 1
    second_sym = idx_sum
print(idx_sum)

# task_19
#
# import math
# sum_of_all_numbers = 0
# for x in range(int(math.pow(1000000, 1/3))+1):
#     x = x**3
#     # if x > 0 and x < 1000000:
#     sum_of_all_numbers = sum_of_all_numbers + x
# print("Сумма всех чисел, которые являются степенью 3ки от 0 до 1000000 равна:", sum_of_all_numbers)
#
# # task_20
#
# for x in range(1000):
#     if '1' in str(x) and '7' in str(x):
#         print(x)

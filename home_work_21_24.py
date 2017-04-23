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

def is_prime(x):
    for i in range(1, x):
        if i <= 2:
            continue
        if x % i == 0 or x % 2 == 0:
            return False
    else:
        return True

# print(isprime(11))

for a in range(1, 101):
    if is_prime(a):
        print(a)


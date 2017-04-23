import random

def avr_random_numbers(num_randoms, lower_limit, upper_limit):
    avr_num = 0
    for i in range(num_randoms):
        num = random.randint(lower_limit, upper_limit)
        # print(num)
        avr_num = avr_num + num
    print("Среднее арифметическое =", avr_num/num_randoms)

avr_random_numbers(10, 0, 10)

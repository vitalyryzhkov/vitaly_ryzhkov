import random
import string
def gen_passw(count_little_lettrs, count_numbers, count_big_letters):
    little_letters = string.ascii_lowercase
    little_letters_lst = []
    for i in range(count_little_lettrs):
        little_letters_lst.append(random.choice(little_letters))
    new_little_letters = "".join(little_letters_lst)

    numbers = string.digits
    num_lst = []
    for x in range(count_numbers):
        num_lst.append(random.choice(numbers))
    new_num = "".join(num_lst)

    big_letters = string.ascii_uppercase
    big_letters_lst = []
    for c in range(count_big_letters):
        big_letters_lst.append(random.choice(big_letters))
    new_big_letters = "".join(big_letters_lst)

    password = new_little_letters + new_num + new_big_letters
    password_lst = list(password)

    random.shuffle(password_lst)
    new_password = "".join(password_lst)
    print(new_password)

gen_passw(3, 3, 2)

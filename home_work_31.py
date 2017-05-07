import random

little_letters = "qwertyuiopasdfghjklzxcvbnm"
little_letters_lst = []
for i in range(3):
    little_letters_lst.append(random.choice(little_letters))
new_little_letters = "".join(little_letters_lst)

num = "0123456789-"
num_lst = []
for x in range(2):
    num_lst.append(random.choice(num))
new_num = "".join(num_lst)

big_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
big_letters_lst = []
for c in range(3):
    big_letters_lst.append(random.choice(big_letters))
new_big_letters = "".join(big_letters_lst)

password = new_little_letters + new_num + new_big_letters
password_lst = list(password)

random.shuffle(password_lst)
new_password = "".join(password_lst)
print(new_password)

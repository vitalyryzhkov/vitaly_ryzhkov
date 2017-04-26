# planets = [' mercury', ' mars', ' earth', ' venus']
#
# def normalize_name_of_planets(planets):
#     for i, elem in enumerate(planets):
#         planets[i] = i[1:]
#     print(planets)
#
# normalize_name_of_planets(planets)

# task_25

lst = [1, 2, 3, 4, 5]
def avr_lst(lst):
    sum_list_elem = 0
    for i in range(len(lst)+1):
        sum_list_elem += i
    print(sum_list_elem/len(lst))
avr_lst(lst)






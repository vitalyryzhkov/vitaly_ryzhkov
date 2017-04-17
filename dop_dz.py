"""
Задача написать функцию, которая определяет надо ли переводить время на час вперед/назад.
Должна вернуть +1, если надо переводить вперед, -1, если назад, 0 - если не надо.
Получает месяц, день недели, день месяца. Т.е.:
``` def daylight_saving (month, week_day, day_of_month)```
"""
# month = "January", "February", "March", "April", "May", "June", "July", "August", \
#         "September", "October", "November", "December"
# week_day = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

def daylight_saving (month, week_day, day_of_month):
    result1 = (month == "March" or month == "march") and (week_day == "Sunday" or week_day == "sunday") and (day_of_month > 24 and day_of_month <= 31)
    result2 = (month == "October" or month == "october") and (week_day == "Sunday" or week_day == "sunday") and (day_of_month > 24 and day_of_month <= 31)
    if result1:
        print("+1")
    elif result2:
        print("-1")
    else:
        print("Часы переводить не нужно")
        return result1, result2
daylight_saving(input("Enter month: "), input("Enter week day: "), int(input("Enter day: ")))
# print(daylight_saving(input("Enter month: "), input("Enter week day: "), int(input("Enter day: "))))

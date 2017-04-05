width = 42.123
height = 43.123345
rect_square = width * height
print("For width %.2f and height %.2f rect sq is: %.2f" %
      (width, height, rect_square))

# print("For width ", width, " and height ", height, "rect sq is: ", rect_square)
# print("Square of rectangle: ", rect_square)


# curr_time = "17:53:42"
# hours = curr_time[:2]
# minutes = curr_time[3:5]
# seconds = curr_time[6:]
# total_seconds = int (hours)*60*60 + int (minutes)*60 + int(seconds)
#
# print(total_seconds)


# curr_time = "1:31:42"
# idx1 = curr_time.find(':')
# hours = curr_time[:idx1]
# print(hours)
#
# idx2 = curr_time.find(':', idx1+1)
# minutes = curr_time[idx1+1 : idx2]
# print(minutes)
#
# seconds = curr_time[idx2+1 : ]
# print(seconds)
# minutes = curr_time[3:5]
# seconds = curr_time[6:]
# total_seconds = int (hours)*60*60 + int (minutes)*60 + int(seconds)
#
# print(total_seconds)

# full_name = "vitaly ryzhkov"
# a = full_name.find(' ')
# name = full_name[: a]
# # print(name)
# s_name = full_name[a+1 :]
# new_name = name + " " + s_name
# print(new_name[ :: - 1])
# print(new_name)


s = "aXXXXXXXXXXb"
first_sym = s[0]
last_sym = s[-1]
middle_str = s[1:-1]
print(last_sym + middle_str + first_sym)


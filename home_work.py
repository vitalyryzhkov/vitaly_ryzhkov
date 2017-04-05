from math import *

# task_1
print("task1")

a = 8
b = 12
c = 7
d = a + b * (c / 2)
print("При условии, что а = %d, b = %d и c = %d, результат d будет равен %g\n"
      % (a, b, c, d))

# print("При условии, что а =", a, ", b =", b, "и c =", c, ",", "d будет равно", d)

# task_2
print("task2")

a = 0.5
b = 55
c = (a**2 + b**2) % 2
print("При условии, что а = %.1f и b = %d, результат c будет равен %g\n"
      % (a, b, c))

# task_3
print("task3")

a = 11
b = -984
c = .12
d = (a + b) / 12 * c % 4 + b
print("При условии, что а = %d, b = %d и c = %.2f, результат d будет равен %.2f\n"
      % (a, b, c, d))

# task_4
print("task4")

a = 289
b = 777
c = 42.
d = (a - b * c) / (a + b) % c
print("При условии, что а = %g, b = %g и c = %.2f, результат d будет равен %.7f\n"
      % (a, b, c, d))

# task_5
print("task5")

a = 12
b = 34
c = 87
d = abs(a - b) / (a + b)**3 - cos(c)
print("При условии, что а = %d, b = %d и c = %d, результат d будет равен %g\n"
      % (a, b, c, d))

# task_6
print("task6")

a = 77
b = 102.1
c = 53
d = (log(1 + c) / -b)**4 + abs(a)
print("При условии, что а = %d, b = %.1f и c = %d, результат d будет равен %g\n"
      % (a, b, c, d))

sym = "aaababac"
new_sym = sym.replace(sym[0], sym[-1])

print(new_sym[:-1] + sym[0])

#  или же можно результат записать в переменную и вывести ее
#  res = new_sym[:-1] + sym[0]
#  print(res)

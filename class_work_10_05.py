# dict_vocab_en_es = {'world': 'mundo', 'language': 'idioma', 'See you later': 'Hasta la vista'}
dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
# dict_planets_2 = {'earth': (345778, 894202), 'mars': (47789, 898902), 'venus': (4679339, 238000)}
# print(dict_planets)

capitals = {'GB': 'London', 'France': 'Paris', 'Ukraine': 'Kyiv'}
cars = {'MB': ['A', 'B', 'G', 'S', 'GLs'], 'BMW': ['3-s', '5-s', '7-s']}
# print(cars['MB'][3])

# dict_planets['mercury'] = 424242
# del dict_planets['venus']
# print(dict_planets)

# capitals['USA'] = 'Washington'
# capitals['USA'] = 'Washington DC'
# cars['AUDI'] = ['A4', 'A6', 'A*8']
# cars['AUDI'].append('A5')
# if 'MB' in cars:
#     tm_cars = cars['MB']
# if 'AUDI' in cars:
#     print(cars)
#     del cars['AUDI']
# print(cars)

# for key in cars:
#     print (key)
#
# for key in cars:
#     print (key, "->", cars[key])
#
# for key, value in cars.items():
#     print ("%s -> %s" % (key, value))
#
# for key in sorted(cars):
#     print (key, "->",  cars[key])
#
# for key in sorted(cars, key=cars.get):# reverse=True):
#     print (key, "->",  cars[key])

employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}

employee_1['address'] = {'city':"Odessa", 'street':'Pyskinska', 'number':1}
employee_2['address'] = {'city':"Kyiv", 'street':'Rish', 'number':17}
employee_3['address'] = {'city':"Lviv", 'street':'Lvivskaya', 'number':7}
employee_4['address'] = {'city':"Mon", 'street':'Deribas', 'number':5}

# employee_1['salary'] *= 1.5
# employee_2['salary'] *= 1.5
# employee_3['salary'] *= 1.5
# employee_4['salary'] *= 1.5

# employees = [employee_1, employee_2, employee_3, employee_4]
#
# for employee in employees:
#     employee['salary'] *= 1.5
#
# print(employees)


planets = [' mercury', ' mars', ' earth', ' venus']

def normalize_name_of_planets(planets):
    for i, elem in enumerate(planets):
        planets[i] = elem[1:]
    print(planets)

normalize_name_of_planets(planets)

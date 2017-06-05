from math import sqrt
import point

class Circle():

    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad

    def is_point_in_circle(self, point):
        distance_between_centers = sqrt(pow((self.x - point.x), 2) + pow((self.y - point.y), 2))
        if distance_between_centers <= self.rad:
            return True
        else:
            return False

point1 = point.Point(8, 7)
circle = Circle(8, 7, 2)
print("Is point in circle?", circle.is_point_in_circle(point1))


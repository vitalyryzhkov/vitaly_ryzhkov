from random import randint


class Godzilla:
    def __init__(self, volume_stomach, count_stomach_full, stomach_full):
        self.volume_stomach = volume_stomach
        self.stomach_full = stomach_full
        self.count_stomach_full = count_stomach_full

    def is_hungry(self, people_weight):
        # count_stomach_full = 0
        if people_weight < self.stomach_full - self.count_stomach_full:
            self.count_stomach_full += people_weight
            print("Godzilla ate", self.count_stomach_full, "kg, peoples meat.....")
            return False
        else:
            print("Godzilla is full and can no longer eat people")
            return True


people_weight = 0
while Godzilla(100, 0, 90).is_hungry(people_weight) == False:
    people_weight = randint(1, 15)

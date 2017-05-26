class Godzilla:
    def __init__(self, volume_stomach):
        self.volume_stomach = volume_stomach

    def eat_peoples(self):
        from random import randint

        stomach_full = self.volume_stomach * 0.9
        count_stomach_full = 0

        while count_stomach_full < int(stomach_full):
            people_weight = randint(1, 95)
            if people_weight > stomach_full - count_stomach_full:
                continue
            count_stomach_full += people_weight
            print("Godzilla ate", count_stomach_full, "kg, peoples meat.....")

        print("Godzilla is full and can no longer eat people")


Godzilla(1000).eat_peoples()

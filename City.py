import math

class City(object):

    def __init__(self, name, loc_x, loc_y, stop_time):
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.stop_time = stop_time

    def __str__(self):
        ET = self.stop_time / 60
        ET = format(ET, '.2f')
        return self.name + " (" + str(self.loc_x) + ", " + str(self.loc_y) + "). Exchange time: " + str(ET) + " minutes"

    def __eq__(self, other):
        if self.loc_x == other.loc_x and self.loc_y == other.loc_y:
            return True
        else:
            return False

    def distance_to_city(self, city):
        dist = math.sqrt((city.loc_x - self.loc_x)**2 + (city.loc_y - self.loc_y)**2)
        return dist
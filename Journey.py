from Train import Train
from City import City

class Journey(object):

    def __init__(self, train, destinations, start_time):
        self.train = train
        self.destinations = destinations
        self.start_time = start_time
        if type(train) is Train:
            pass
        else:
            raise TypeError("Not a Train object")
        if type(destinations) is list:
            pass
        else:
            raise TypeError("Destinations not a list")

    def __str__(self):
        i = 0
        DestLen = len(self.destinations)
        TheString = "Journey with " + str(DestLen) + " stops:\n"
        for x in self.destinations:
            TheString = TheString + "\t" + self.destinations[i].__str__() + "\n"
            i = i + 1
        TheString = TheString + "Train Information: " + self.train.__str__()

        return TheString

    def add_destination(self, city):

        self.destinations.append(city)

    def city_in_journey(self, city):
        Hit = False
        for x in self.destinations:
            if city == x:
                Hit = True
        return Hit

    def check_journey_includes(self, start_city, dest_city):
        Hit = False
        i = 0
        for x in self.destinations:
            i += 1
            if start_city.name == x.name:
                while i <= len(self.destinations) -1:
                    if i <= len(self.destinations):
                        if dest_city.name == self.destinations[i].name:
                            Hit = True
                            break
                    else:
                        break
                    i += 1
        return Hit

    def total_journey_distance(self):
        TotalDist = 0
        i = 1
        if len(self.destinations) == 1:
            return TotalDist
        else:
            for x in self.destinations:
                if i < len(self.destinations):
                    TotalDist = TotalDist + x.distance_to_city(self.destinations[i])
                    i += 1
            return TotalDist
    
    def city_arrival_time(self, city):
        TotalArrivalTime = 0
        StartTime = 0
        Dist = 0
        FPS = 0
        Total = 0
        j = 1
    
        if len(self.destinations) == 1:
            Total = self.start_time
        else:
            #StartTime = self.start_time + self.destinations[0].stop_time
            #FPS = self.train.speed_fps
            #Dist = (self.destinations[0].distance_to_city(self.destinations[1])) / FPS
            #Total = StartTime + Dist

            StartTime = self.start_time + self.destinations[0].stop_time
            FPS = self.train.speed_fps
            for x in self.destinations:
                Dist = (x.distance_to_city(self.destinations[j])) / FPS
                j += j
                Total = StartTime + Dist
    

            
    

        return Total

    

    def city_departure_time(self, city):
        return ""

    def total_journey_time(self):
        fedsa=5432
        return ""

    def all_passengers_accommodated(self, unload_list, load_list):
        Hit = True
        for x in self.destinations:
            for y in unload_list:
                try:
                    self.train.unload_passengers(y)
                    qqq = self.train.num_passengers
                except:
                    Hit = False
                    return Hit
            for z in load_list:
                try:
                    self.train.load_passengers(z)
                    ttt = self.train.num_passengers
                except:
                    Hit = False
                    return Hit
        return Hit
from TrainCapacityException import TrainCapacityException
class Train(object):

    def __init__(self, name, max_passengers, speed_fps):
        self.name = name
        self.max_passengers = max_passengers
        self.num_passengers = 0
        self.speed_fps = speed_fps

    def __str__(self):
        return str("Train named " + self.name + " with " + str(self.num_passengers) + " passengers will travel at " + str(self.speed_fps) + " mph")

    def time_to_travel(self, distance_feet):
        self.travel_time_final = int((distance_feet / self.speed_fps))
        return self.travel_time_final

    def load_passengers(self, num_people):
        combined_total = num_people + self.num_passengers

        if combined_total <= self.max_passengers:
            self.num_passengers = combined_total
            #return str(self.num_passengers) + " passengers are currently on the train!"
        else:
            Leftout = combined_total - self.max_passengers
            raise TrainCapacityException(Leftout, "full")

    def unload_passengers(self, num_people):
        
        if num_people <= self.num_passengers:
            diff = self.num_passengers - num_people
            self.num_passengers = diff
            return str(num_people) + " passengers are removed from the train!"
        else:
            diff = num_people - self.num_passengers 
            raise TrainCapacityException(diff, "empty")
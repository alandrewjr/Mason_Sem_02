class TrainCapacityException(Exception):

    def __init__(self, number, issue):
        self.number = number
        self.issue = issue
        
    def __str__(self):
        if self.issue == "full":
            return str(self.number) + " passengers cannot be loaded because the train is " + self.issue + "!"
        else:
            return str(self.number) + " passengers cannot be unloaded because the train is " + self.issue + "!"



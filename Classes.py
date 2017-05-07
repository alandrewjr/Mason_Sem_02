from Train import Train
from City import City
from Journey import Journey
from TrainCapacityException import TrainCapacityException

def aa_test():
    MyTrain = Train("Chuggington", 100, 22) #(name, max passengers, fps)
    MyCity1 = City("Philly", 9, 20, 50)
    name = MyTrain.name
    MyTrain.num_passengers = 60
    #LoadPassengers = MyTrain.load_passengers(5)
    #TimeTravel = MyTrain.time_to_travel(2200)
    UnloadPassengers = MyTrain.unload_passengers(50)
    
    #print(name)
    #print(MyTrain)
   # print(LoadPassengers)
    #print(TimeTravel)

    #print(TrainCapacityException(5,"full"))
    #print(TrainCapacityException(15,"empty"))
    #print(UnloadPassengers)

    #print(MyCity.distance_to_city("fairfax"))
    #MyCity2 = City("Vegas", 9, 22, 100)
    #print(MyCity1.__eq__(MyCity2))

    #MyTrain1 = ""
    Journey1 = Journey(MyTrain1, "gfagfgagf", 4000)

#region aa_test()
#aa_test()
#endregion

def NewTrain():
    MyTrain = Train("Chuggington", 100, 22) #(name, max passengers, fps)
    print(MyTrain.name)
    print(MyTrain.max_passengers)
    print(MyTrain.speed_fps)
    print(MyTrain.num_passengers)
    MyTrain.num_passengers = 33
    print(MyTrain.num_passengers)

#region NewTrain
#NewTrain()
#endregion

def LoadPassengers(n):
    #MyTrain = Train("Wally", 100, 22) #(name, max passengers, fps)
    #MyTrain.num_passengers = 40
    #print(MyTrain.name)
    #MyTrain.load_passengers(n)
    #print(MyTrain.num_passengers)
    #MyTrain.load_passengers(45)
    #print(MyTrain.num_passengers)

    train = Train("train 1", 50, 22)
    train.load_passengers(20)
    train.load_passengers(30)
    print(train.num_passengers)

#region LoadPassengers
#LoadPassengers(20)
#LoadPassengers(30)
#endregion

def UnloadPassengers(n):
    #MyTrain = Train("Chuggington", 100, 22) #(name, max passengers, fps)
    #print(MyTrain.max_passengers)
    #Result = MyTrain.unload_passengers(n)
    #print(Result)
    train = Train("train 1", 50, 22)
    train.num_passengers= 40
    train.unload_passengers(25)
    train.unload_passengers(5)
    train.unload_passengers(10)

#region UnloadPassengers
#UnloadPassengers(50)
#endregion

def UnloadPassException():
    train = Train("train 1", 10, 22)
    train.load_passengers(10)
    try:
        train.unload_passengers(16)
    except TrainCapacityException as e:
        #print(e.__str__())
        print(e.number)

#region UnloadPassException
#UnloadPassException()
#endregion

def TrainTimeTravel():
    MyTrain = Train("Flo", 100, 22) #(name, max passengers, fps)
    print(MyTrain.time_to_travel(100))

#region TrainTimeTravel
#TrainTimeTravel()
#endregion

def TrainTestSTR():
    MyTrain = Train("Mary", 333, 190) #(name, max passengers, fps)
    MyTrain.load_passengers(78)
    print(MyTrain)

#region TrainTestSTR
#TrainTestSTR()
#endregion

def NewCity():
    MyCity1 = City("Philly", 9, 20, 50)
    print(MyCity1.loc_x)
    print(MyCity1.loc_y)
    print(MyCity1.name)
    print(MyCity1.stop_time)
    print(MyCity1)

#region NewCity
#NewCity()
#endregion

def CityEQ():
    MyCity1 = City("Jersey", 9, 20, 50)
    MyCity2 = City("Vegas", 9, 22, 100)
    print(MyCity1.__eq__(MyCity2))
    MyCity3= City("Vegas", 9, 22, 100)
    print(MyCity2.__eq__(MyCity3))
    MyCity4 = City("Atco", 9, 20, 50)
    print(MyCity1.__eq__(MyCity4))

#region CityEQ
#CityEQ()
#endregion

def CityDistance():
    c1 = City("City 1",2,3,300)
    c2 = City("City 2",0,8,300)
    print(c1.distance_to_city(c2)) # 5

#region CityDistance
#CityDistance()
#endregion

def CityTestSTR():
    c1 = City("City 1",0,3,300)
    print(c1)

#region CityTestSTR
#CityTestSTR()
#endregion

def NewJourney():
    #MyTrain = Train("Norman", 100, 22) #(name, max passengers, fps)
    #Journey1 = Journey(MyTrain, ["xxx", "yyy"], 4000)
    #print(Journey1)

    #MyTrain1 = ""
    #Journey2 = Journey(MyTrain1, ["aaa", "bbb"], 4000)
    #print(Journey2)

    t = Train("Express One", 50, 100)
    j = Journey(t, [], 0)
    print(j.__str__())
    #print(j.__init__())

#region NewJourney
#NewJourney()
#endregion

def JourneyTestSTR():
    t = Train("Express One", 50, 100)
    c1 = City("City 1",5,10,600)
    c2 = City("City 2",2,3,900)
    c3 = City("City 3", 0,0,300)
    c4 = City("City 4", 12,4,1000)
    j = Journey(t,[c1,c2,c3,c4],200)

    #MyTrain = Train("Norman", 324, 65) #(name, max passengers, fps)
    #Journey1 = Journey(MyTrain, ["aaa", "bbb", "ccc", "ddd", "eee", "fff"], 4060)
    print(j)

#region JourneyTestSTR
#JourneyTestSTR()
#endregion

def AddDest():
    t = Train("Express One", 50, 100)
    c1 = City("City 1",5,10,600)
    c2 = City("City 2",2,3,900)
    j = Journey(t,[c1,c2],200)
    print(j)
    ct = City("City 3", 8, 4, 440)
    j.add_destination(ct)
    print(j)

#region AddDest()
#AddDest()
#endregion

def CityInJourney():
    t = Train("Express One", 50, 100)
    c1 = City("City 1",5,10,600)
    cities = [c1,City("City 2",2,3,900), City("City 3",0,0,300)]
    j = Journey(t,cities,200)
    r = j.city_in_journey(c1)
    print(r)
    print(j.city_in_journey("City 1"))

#region CityInJourney()
#CityInJourney()
#endregion

def CheckJourney():
    #t = Train("Express One", 50, 100)
    #c1 = City("City 1",5,10,600)
    #c2 = City("City 2",2,3,900)
    #c3 = City("City 3", 0,0,300)
    #c4 = City("City 4", 12,4,1000)
    #c5 = City("City 5", 12,4,1000)
    #j = Journey(t,[c1,c2,c3,c4],200)
    #print(j.check_journey_includes(c5,c2))

    t = Train("Express One", 50, 100)
    c1 = City("City 1",5,10,600)
    c2 = City("City 2",2,3,900)
    c3 = City("City 3", 0,0,300)
    c4 = City("City 4", 12,4,1000)
    j = Journey(t,[c1,c2,c3,c4],200)
    print(j.check_journey_includes(c3,c2))

#region CheckJourney
#CheckJourney()
#endregion

def TotalJourneyDistance():
    #t = Train("Express One", 50, 100)
    #c1 = City("City 1",0,3,300)
    #j = Journey(t,[c1],200)
    #print(j.total_journey_distance()) # 0

    t = Train("Express One", 50, 100)
    c1 = City("City 1",0,3,300)
    c2 = City("City 2",0,8,300)
    j = Journey(t,[c1,c2],200)
    print(j.total_journey_distance()) # 5

#region TotalJourneyDistance
#TotalJourneyDistance()
#endregion

def city_arrival_time():
    #t = Train("Express One", 50, 100)
    #c1 = City("City 1",0,3,300)
    #j = Journey(t,[c1],200)
    #print(j.city_arrival_time(c1)) # 200

    #t = Train("Express One", 50, 10)
    #c1 = City("City 1",0,3,300)
    #c2 = City("City 2",0,3003,300)
    #j = Journey(t,[c1,c2],200)
    #print(j.city_arrival_time(c2)) # 800

    #t = Train("Express One", 50, 10)
    #c1 = City("City 1",100,3,120)
    #c2 = City("City 2",78,300,300)
    #j = Journey(t,[c1,c2],1000)
    #print(j.city_arrival_time(c1)) #,1000
    ##print(j.city_arrival_time(c2)) # 1149

    t = Train("Express One", 50, 10)
    c1 = City("City 1",100,3,120)
    c2 = City("City 2",78,300,300)
    c3 = City("City 3", 50, 100, 240)
    j = Journey(t,[c1,c2,c3],1000)
    print(j.city_arrival_time(c3)) # 1469

#region city_arrival_time(self, city)
#city_arrival_time()
#endregion


def AllPassengersAccommodated():
    #t = Train("Express One", 50, 100)
    #c1 = City("City 1",0,3,300)
    #j = Journey(t,[c1],200)
    #print(j.all_passengers_accommodated([5],[5])) # False #no passenger to be unloaded

    #t = Train("Express One", 50, 100)
    #c1 = City("City 1",0,3,300)
    #j = Journey(t,[c1],200)
    #print(j.all_passengers_accommodated([0],[100])) # False) #too many to load
  
    #t = Train("Express One", 50, 10)
    #c1 = City("City 1",0,3,300)
    #j = Journey(t,[c1],200)
    #print(j.all_passengers_accommodated([0],[30])) # ,True)

    t = Train("Express One", 50, 10)
    c1 = City("City 1",0,3,300)
    c2 = City("City 2",78,300,300)
    j = Journey(t,[c1,c2],200)
    print(j.all_passengers_accommodated([0,40],[30,10])) #,False)

#region AllPassengersAccommodated
#AllPassengersAccommodated()
#endregion

def total_journey_time():
    t = Train("Express One", 50, 100)
    c1 = City("City 1",0,3,300)
    j = Journey(t,[c1],200)
    print(j.total_journey_time()) #,300)
    
    t = Train("Express One", 50, 10)
    c1 = City("City 1",0,3,300)
    c2 = City("City 2",0,3003,300)
    j = Journey(t,[c1,c2],200)
    print(j.total_journey_time()) #,900)

#region total_journey_time(self)
total_journey_time()
#endregion
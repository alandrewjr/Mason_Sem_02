RootPath = "C:\\Users\\Albert\\Downloads\\p5\\p5\\"
RFN = "SampFile1.csv"
STF = "SampStatFile.csv"
INFOFILE = "AA_INFOFILE.csv"
INFO_FILE = {}
STATS_FILE = {}

def info_db1():
	return {'Bulbasaur':(1,'Grass','Poison',1,False)}

db1 = {'Bulbasaur':(1,'Grass','Poison',1,False)}


def test_new_dict():
    OldDict = db1
    NewDict = {}
    NewDict = OldDict
    
    print(OldDict)
    print(NewDict)
#region test_new_dict
#test_new_dict()
#endregion

def test_dict(d):
    
    if d:
        return True
    else:
        return False
#print(test_dict(INFO_FILE))

def parser(f):
    NewString = ""
    QuoteHit = 0
    NewList = []
    #FileLoc = open(RootPath + f, 'r')
    #Line1 = FileLoc.readline()
    #Line2  = FileLoc.readline()
    #for x in Line2:
    for x in f[:-1]:
        if (x == "," and QuoteHit == 0):
            NewList.append(NewString)
            NewString = ""
            QuoteHit = 0
        elif (x == "\""):
            QuoteHit = QuoteHit + 1
            if QuoteHit == 2:
                QuoteHit = 0
        else:
            NewString = NewString + x
    
    NewList.append(NewString)
    str(NewList).replace(' ', '')
    return NewList

#region reader1
#print(parser("SampFile1.csv"))
#endregion

def read_info_file_AA(filename):
    FileLoc = open(RootPath + filename, 'r')

    #li = FileLoc.readline()
    
    #l2 = FileLoc.readline()

    Lines = FileLoc.readlines()
    ReadList = []
    Words = []
    INFO_FILE = {}
#INFO_FILE["name"] = INFO_TUPLE
    idx = 0
    DataRow = Lines[1].split(',')
    #region TooMuch
    #print('xxx\n', FileLoc.readlines())
    #for eachLine in Lines:
    #    #print(eachLine)
    #    DataRow = Lines[idx].split(',')
    #    #words = data.split(',')
    #    for item in DataRow:
    #        dd = item
    #    idx = idx + 1
 
    #FileLoc.close()
    
    #HeaderLine = Lines[0].split(',')
    #DataRow = Lines[1].split(',')

    #for data in Lines:
    #    DataRow = Lines[idx].split(',')
    #    #words = data.split(',')
    #    for item in DataRow:
    #        dd = item
    #    idx = idx + 1

    #INFO_TUPLE = (DataRow[0],DataRow[2],DataRow[3],DataRow[4],DataRow[5])
    #INFO_FILE[DataRow[1]] = INFO_TUPLE
    #endregion
    with open(RootPath + filename) as Lines:
        next(Lines)
        for x in Lines:
            x = x.split(',')
            #x = x[1:-1]
            x[-1] = x[-1].strip('"\n')
            ReadList.append(x)
    for item in ReadList:
        INFO_TUPLE = (int(item[0].replace("\"", '')),item[2].replace("\"", ''),item[3].replace("\"", ''),item[4].replace("\"", ''),item[5].replace("\"", ''))
        INFO_FILE[item[1].replace("\"", '')] = INFO_TUPLE

    #for x in Lines:
    #    #words = x.split(',')
    #    #word1 = words[1]
    #    HeaderLine = Lines[0].split(',')
    #    DataRow = Lines[idx].split(',')
    #    INFO_TUPLE = (DataRow[0],DataRow[2],DataRow[3],DataRow[4],DataRow[5])
    #    INFO_FILE[DataRow[1]] = INFO_TUPLE
    #    print(x, end="")
    #    idx = idx + 1
    #    #print(x)
    #FileLoc.close()    
    return INFO_FILE

def read_info_file(filename):
    FileLoc = open(RootPath + filename, 'r')
    
    FormattedList = []
    LinInt = 1
    Line1 = FileLoc.readline()
    Lines = FileLoc.readlines()
    for line in Lines:
        MyList = parser(line)
        ID = int(MyList[0])
        Name = MyList[1]
        if (MyList[2] == ""):
            Type1 = None
        else:
            Type1 = MyList[2]
        if (MyList[3] == ""):
            Type2 = None
        else:
            Type2 = MyList[3]
        Generation = int(MyList[4])
        if MyList[5] == "TRUE":
            Legendary = True
        else:
            Legendary = False
        INFO_TUPLE = (ID,Type1,Type2,Generation,Legendary)
        INFO_FILE[Name] = INFO_TUPLE
    FileLoc.close()

    #OutFile = open(RootPath + INFOFILE, 'w')
    #OutFile.write(str(INFO_FILE).replace(' ',''))
    #OutFile.close()

    #Lines = FileLoc.readlines()
    #ReadList = []
    ##INFO_FILE = {}
    
    #with open(RootPath + filename) as Lines:
    #    next(Lines)
    #    for x in Lines:
    #        x = x.split(',')
    #        x[-1] = x[-1].strip('"\n')
    #        ReadList.append(x)
    #for item in ReadList:
    #    MyBoolTest = item[5].replace("\"", '')
    #    MyNewBool = True
    #    if MyBoolTest == "FALSE":
    #        MyNewBool = False
    #    TestForNone = item[3].replace("\"", '')
    #    if TestForNone == '':
    #        TestForNone = None
    #    INFO_TUPLE = (int(item[0].replace("\"", '')),item[2].replace("\"", ''),TestForNone,int(item[4].replace("\"", '')),MyNewBool)
    #    INFO_FILE[item[1].replace("\"", '')] = INFO_TUPLE
    return INFO_FILE

#region read_info_file
#print(read_info_file_AA("info_file1.csv"))

print(read_info_file(RFN))

#print(read_info_file("SampFile1.csv"))
#print(read_info_file("info_file1.csv"),"\n",info_db1())
#endregion

def read_stats_file(filename):
    FileLoc = open(RootPath + filename, 'r')
    Lines = FileLoc.readlines()
    ReadList = []
    #STATS_FILE = {}
    
    with open(RootPath + filename) as Lines:
        next(Lines)
        for x in Lines:
            x = x.split(',')
            x[-1] = x[-1].strip('"\n')
            ReadList.append(x)
    for item in ReadList:
        STATS_TUPLE = (int(item[1]),int(item[2]),int(item[3]),int(item[4]))
        STATS_FILE[int(item[0])] = STATS_TUPLE
    return STATS_FILE

#region read_stats_file
#print(read_stats_file("stats_file1.csv"))
#print(read_stats_file("stats_file2.csv"))
#print(read_stats_file("stats_file3.csv"))
#print(read_stats_file(STF))
#endregion

def combine_databases(info_db, stats_db):
    List1 = []
    Tuple1 = ()
    Merged = {}

    if (info_db and stats_db):
        for key, value in info_db.items():
            Infokey = key
            ItemList = value
            List1 = list(ItemList)
            ItemID = ItemList[0]
            z = 3
            if ItemID in stats_db:
                StatsDBItems = stats_db[ItemID]
                for x in StatsDBItems:
                    List1.insert(z, x)
                    z = z + 1
                Tuple1 = tuple(List1)
                Merged[Infokey] = Tuple1

                #for key1, value1 in stats_db.items():
                #    Items = value1
                #    for x in Items:
                #        List1.insert(3, x)
                #Tuple1 = tuple(List1)
                #Merged[Infokey] = Tuple1
    return Merged

#region combine_databases
#read_info_file(RFN)
#read_stats_file(STF)
#print(combine_databases(INFO_FILE,STATS_FILE))
#endregion

def pokemon_by_types(db, types):
    List1 = []
    Tuple1 = ()
    TypeDict = {}
    for x in types:
        for key, value in db.items():
            Infokey = key
            ItemList = value
            List1 = list(ItemList)
            ItemID = ItemList[0]
            if x in ItemList:
                Tuple1 = tuple(List1)
                TypeDict[Infokey] = Tuple1
    return TypeDict

#region pokemon_by_types
#read_info_file(RFN)
#read_stats_file(STF)
#print(pokemon_by_types(combine_databases(INFO_FILE,STATS_FILE), ["Grass"]))
##print(pokemon_by_types(combine_databases(INFO_FILE,STATS_FILE), ["Poison","Flying", "Ghost"]))
#print(pokemon_by_types(combine_databases(INFO_FILE,STATS_FILE), [None]))
#endregion

def pokemon_by_hp_defense(db, lowest_hp, lowest_defense):
    List1 = []
    Tuple1 = ()
    LowDict = {}
    for key, value in db.items():
        Infokey = key
        ItemList = value
        List1 = list(ItemList)
        ItemID = ItemList[0]
        HP = ItemList[3]
        Def = ItemList[5]
        if HP >= lowest_hp and Def >= lowest_defense:
            Tuple1 = tuple(List1)
            LowDict[Infokey] = Tuple1
    return LowDict

#region pokemon_by_hp_defense
#read_info_file(RFN)
#read_stats_file(STF)
#print(pokemon_by_hp_defense(combine_databases(INFO_FILE,STATS_FILE), 90, 93))
#endregion

def get_types(db):
    TypesList = []
    SetList = []
    for key, value in db.items():
        Infokey = key
        ItemList = value
        Type1 = ItemList[1]
        Type2 = ItemList[2]
        if Type1 is not None:
            TypesList.append(Type1)
        if Type2 is not None:
            TypesList.append(Type2)
    TypesList.sort()
    SetList = list(set(TypesList))
    SetList.sort()
    return SetList

#region get_types
#read_info_file(RFN)
#read_stats_file(STF)
#print(get_types(combine_databases(INFO_FILE,STATS_FILE)))
#endregion

def count_by_type(db,type):
    ResultsTuple = ()
    SingleCount = 0
    DualCounter = 0
    Total = 0
    for key, value in db.items():
        Infokey = key
        ItemList = value
        Type1 = ItemList[1]
        Type2 = ItemList[2]
        if Type1 == type:
            if Type2 is None:
                SingleCount = SingleCount + 1
            else:
                DualCounter = DualCounter + 1
        else:
            if Type2 == type:
                if Type1 is None:
                    SingleCount = SingleCount + 1
                else:
                    DualCounter = DualCounter + 1
    Total = SingleCount + DualCounter
    ResultsTuple = (SingleCount, DualCounter, Total)
    return ResultsTuple
    
#region count_by_type
#read_info_file(RFN)
#read_stats_file(STF)
#print(count_by_type(combine_databases(INFO_FILE,STATS_FILE), "Poison"))
#endregion

def fastest_type(db):
    AllTypes = get_types(db)
    LookupType = []
    SpeedList = []
    #SpeedList2 = []
    TempDict = {}
    HitCounter = 0
    SpeedTotals = 0
    SpeedAVG = 0
    SpeedTuple = ()
    x_speed = 0
    FinalTypeList = []
    for x in AllTypes:
        LookupType.append(x)
        TempDict = pokemon_by_types(db, LookupType)
        for key, value in TempDict.items():
            Infokey = key
            ItemList = value
            Speed = ItemList[6]
            SpeedTotals = SpeedTotals + Speed
            HitCounter = HitCounter + 1
        SpeedAVG = int(SpeedTotals / HitCounter)
        HitCounter = 0
        SpeedTotals = 0
        LookupType.clear()
        SpeedTuple= (SpeedAVG,x)
        SpeedList.append(SpeedTuple)
    SpeedList.sort(reverse=True)
    for x in SpeedList:
        if x[0] >= x_speed:
            x_speed = x[0]
            FinalTypeList.append(x[1])
        else:
            break
        #region fold
        #LookupType.append(x) 
        #DB1 = pokemon_by_types(db,LookupType)
        #for key, value in DB1.items():
        #    Infokey = key
        #    ItemList = value
        #    List1 = list(ItemList)
        #    ItemID = ItemList[0]
        #    Speed = ItemList[6]
        #    SpeedList.append(Speed)
        #SpeedListLen = len(SpeedList)
        #SpeedListSum = sum(SpeedList)
        #SpeedListAvg = SpeedListSum / SpeedListLen
        #SpeedList.clear()
        #SpeedList.append(int(SpeedListAvg))
        #Tuple1 = tuple(SpeedList)
        #SpeedDict[Infokey] = Tuple1
        #LookupType.clear()
        #endregion
    FinalTypeList.sort()
    return FinalTypeList

#region fastest_type
#read_info_file(RFN)
#read_stats_file(STF)
#print(fastest_type(combine_databases(INFO_FILE,STATS_FILE)))
#endregion

def legendary_count_of_types(db):
    AllTypes = get_types(db)
    LookupType = []
    LegendaryDict = {}
    TypeCounter = 0
    if db:
        for x in AllTypes:
            LookupType.append(x)
            TempDict = pokemon_by_types(db, LookupType)
            for key, value in TempDict.items():
                if value[8] is True:
                    TypeCounter = TypeCounter + 1
            if TypeCounter > 0:
                LegendaryDict[x] = TypeCounter
            TypeCounter = 0
            LookupType.clear()
    return LegendaryDict

#region legendary_count_of_type
#read_info_file(RFN)
#read_stats_file(STF)
#print(legendary_count_of_types(combine_databases(INFO_FILE,STATS_FILE)))
#endregion

def team_hp(db, team):
    TotalHP = 0
    for x in team:
        for key, value in db.items():
            Infokey = key
            ItemList = value
            List1 = list(ItemList)
            ItemID = ItemList[0]
            if x == Infokey:
                HP = List1[3]
                TotalHP = TotalHP + HP
    return TotalHP

#region team_hp
#read_info_file(RFN)
#read_stats_file(STF)
#print(team_hp(combine_databases(INFO_FILE,STATS_FILE), ['Test3','Bulbasaur','Andrew, Jenna','Arceus']))
#print(team_hp(combine_databases(INFO_FILE,STATS_FILE), ['Test13, D']))
#endregion

def show_of_strength_game(db, team1, team2):
    Team1AttackList = []
    Team2AttackList = []
    Team1AttackListLEN = 0
    Team2AttackListLEN = 0
    Team1AttackTotal = 0
    Team2AttackTotal = 0
    ATT1 = 0
    ATT2 = 0
    Winner = 0

    #Team1
    for x1 in team1:
        for key, value in db.items():
            Infokey1 = key
            ItemList1 = value
            List1 = list(ItemList1)
            if x1 == Infokey1:
                Team1AttackList.append(List1[4])
    #Team2
    for x2 in team2:
        for key, value in db.items():
            Infokey2 = key
            ItemList2 = value
            List2 = list(ItemList2)
            if x2 == Infokey2:
                Team2AttackList.append(List2[4])

    Team1AttackListLEN = len(Team1AttackList)
    Team2AttackListLEN= len(Team2AttackList)

    if len(Team1AttackList) > len(Team2AttackList):
        while len(Team1AttackList) > len(Team2AttackList):
            Team2AttackList.append(0)
    else:
        if len(Team2AttackList) > len(Team1AttackList):
            while len(Team2AttackList) > len(Team1AttackList):
                Team1AttackList.append(0)
    
    for i in range(Team1AttackListLEN):
        ATT1 = Team1AttackList[i]
        ATT2 = Team2AttackList[i]
        if ATT1 > ATT2:
            Team1AttackTotal = Team1AttackTotal + 1
        else:
            if ATT1 < ATT2:
                Team2AttackTotal = Team2AttackTotal + 1
    Winner = Team1AttackTotal - Team2AttackTotal
    
    return Winner

#region show_of_strength_game
#read_info_file(RFN)
#read_stats_file(STF)
##print(show_of_strength_game(combine_databases(INFO_FILE,STATS_FILE), ['Test3','Bulbasaur','Andrew, Jenna','Arceus'], ['Reshiram','Test8','HoopaHoopa, Confined']))
#print(show_of_strength_game(combine_databases(INFO_FILE,STATS_FILE), ['Andrew, Jenna', 'Bulbasaur'], ['HoopaHoopa, Confined']))
#endregion

def strongest_pokemon(db, type, generation):
    HPTotal = 0
    AttackTotal = 0
    DefenseTotal = 0
    GrandTotal = 0
    TotalTuple = ()
    NewDict = {}
    NewList = []

    for key, value in db.items():
            Infokey = key
            ItemList = value
            HPTotal = HPTotal + ItemList[3]
            AttackTotal = AttackTotal + ItemList[4]
            DefenseTotal = DefenseTotal + ItemList[5]
            GrandTotal = HPTotal + AttackTotal + DefenseTotal
            #NewDict[Infokey] = GrandTotal
            TotalTuple = (GrandTotal, Infokey, ItemList[1], ItemList[2], ItemList[7])
            NewList.append(TotalTuple)
            HPTotal = 0
            AttackTotal = 0
            DefenseTotal = 0
            GrandTotal = 0
            
    NewList.sort(reverse=True)

    return NewList

#region strongest_pokemon(db, type = None, generation = None):
#read_info_file(RFN)
#read_stats_file(STF)
#print(strongest_pokemon(combine_databases(INFO_FILE,STATS_FILE),None,None))

#endregion


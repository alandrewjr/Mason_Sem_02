def get_rate(start_hr, start_min, day, is_holiday):
    Rate1 = 3
    Rate2 = 4
    Rate3 = 5
    Rate4 = 6
    Result = 0
    StartFlagEarly = False
    if(start_hr == 18):
        if(start_min <= 29):
            StartFlagEarly = True
    elif(start_hr < 18):
        StartFlagEarly = True
#    return StartFlagEarly
        
    if(day == 1 or day <= 4):
        if(StartFlagEarly == True):
            Result = Rate1
        else:
            Result = Rate3
    elif(day == 5):
        if(StartFlagEarly == True):
            Result = Rate1
        else:
            Result = Rate4
    elif(day == 6 or day == 7):
        if(StartFlagEarly == True):
            Result = Rate2
        else:
            Result = Rate4
#    elif(day > 7 or day == 0):
#        Result = 0
    if(is_holiday == True):
        if(StartFlagEarly == True):
            Result = Rate2
        else:
            Result = Rate4
    return Result
#print(get_rate(19,45,4,False))

def check_nite(start_hr, start_min, day):
    NiteSpecialFlag = False

    if(day == 1 or day <= 5):
        if(start_hr == 21):
            if(start_min <= 29):
                NiteSpecialFlag = False
            else:
                NiteSpecialFlag = True
        elif(start_hr < 21):
            NiteSpecialFlag = False
        else:
            NiteSpecialFlag = True

    return NiteSpecialFlag
#print(check_nite(23,0,2))

def get_fee(rate, num_games, num_people, day, is_nite, is_holiday):
    TheRate = 0
    CheckRate1 = 0
    CheckRate2 = 0
    
    if(is_holiday):
        TheRate = (rate * num_people) * num_games
    else:
        if(is_nite == True):
            CheckRate1 = (rate * num_people) * num_games
            if(day == 1 or day <= 4):
                CheckRate2 = 7 * num_people
                if(CheckRate1 < CheckRate2):
                    TheRate = CheckRate1
                else:
                    TheRate = CheckRate2
                #if(rate < 7):
                #    TheRate = rate * num_people
                #else:
                #    TheRate = 7 * num_people
            elif(day == 5):
                CheckRate2 = 14 * num_people
                if(CheckRate1 < CheckRate2):
                    TheRate = CheckRate1
                else:
                    TheRate = CheckRate2
                #if(rate < 14):
                #    TheRate = rate * num_people
                #else:
                #    TheRate = 14 * num_people
        elif(day == 7):
            if(num_people >= 4):
                TheRate = (2 * num_people) * num_games
            else:
                TheRate = (rate * num_people) * num_games
        else:
            TheRate = (rate * num_people) * num_games
    return TheRate

#region Test cases
#print(get_fee(6,2,4,4,True,True))
#print(get_fee(5,2,4,4,True,False))
##print(get_fee(5,1,2,4,True,False))
#print(get_fee(6,4,4,7,False,False))
#print(get_fee(4,2,4,7,False,False))
#print(get_fee(3, 5, 2, 4, False, False))
#print(get_fee(3, 5, 2, 4, False, False))
#print(get_fee(3, 10, 10, 1, False, False))
#print(get_fee(4, 2, 4, 7, False, False))
#print(get_fee(6, 2, 3, 5, True, False))
#print(get_fee(5, 1, 4, 3, True, False))
#print(get_fee(6, 3, 3, 5, True, False))
#print(get_fee(6, 2, 3, 5, True, False))
#print(get_fee(6, 2, 3, 7, False, False))
#print(get_fee(6, 3, 10, 7, False, False))

#print(get_fee(3, 5, 2, 4, False, False))# "your total is $30.")
#print(get_fee(3, 5, 2, 4, False, False))# "your total is $30.")
#print(get_fee(3, 10, 10, 1, False, False))# "your total is $300.")
#print(get_fee(5, 1, 1, 2, False, False))# "your total is $5.")
#print(get_fee(3, 2, 4, 5, False, False))# "your total is $24.")
#print(get_fee(6, 2, 4, 5, False, False))# "your total is $48.")
#print(get_fee(4, 3, 3, 6, False, False))# "your total is $36.")
#print(get_fee(6, 3, 3, 6, False, False))# "your total is $54.")
#print(get_fee(4, 5, 2, 4, False, True))# "happy holidays! your total is $40.")
#print(get_fee(6, 5, 2, 4, False, True))# "happy holidays! your total is $60.")
#print(get_fee(6, 5, 2, 4, True, True))# "happy holidays! your total is $60.")
#print(get_fee(4, 2, 4, 5, False, True))# "happy holidays! your total is $32.")
#print(get_fee(6, 2, 4, 5, False, True))# "happy holidays! your total is $48.")
#print(get_fee(6, 2, 4, 5, True, True))# "happy holidays! your total is $48.")
#print(get_fee(4, 3, 3, 6, False, True))# "happy holidays! your total is $36.")
#print(get_fee(6, 3, 3, 6, False, True))# "happy holidays! your total is $54.")
#print(get_fee(4, 1, 5, 7, False, True))# "happy holidays! your total is $20.")
#print(get_fee(6, 1, 5, 7, False, True))# "happy holidays! your total is $30.")
#print(get_fee(4, 2, 2, 7, False, False))# "your total is $16.")
#print(get_fee(4, 2, 4, 7, False, False))# "thrifty sunday! your total is $16.")
#print(get_fee(6, 2, 3, 7, False, False))# "your total is $36.")
#print(get_fee(6, 3, 10, 7, False, False))# "thrifty sunday! your total is $60.")
#print(get_fee(5, 1, 4, 3, False, False))# "your total is $20.")
#print(get_fee(5, 1, 4, 3, True, False))# "your total is $20.")
#print(get_fee(5, 2, 4, 3, False, False))# "your total is $40.")
#print(get_fee(5, 2, 4, 3, True, False))# "nite special! your total is $28.")
#print(get_fee(6, 2, 3, 5, False, False))# "your total is $36.")
#print(get_fee(6, 2, 3, 5, True, False))# "your total is $36.")
#print(get_fee(6, 3, 3, 5, False, False))# "your total is $54.")
#print(get_fee(6, 3, 3, 5, True, False))# "nite special! your total is $42.")
#print(get_fee(6, 3, 3, 5, False, False))# "your total is $54.")
#print(get_fee(6, 3, 3, 5, True, False))# "nite special! your total is $42.")
#endregion

def price_chart(num_games, num_people, day, is_holiday):
    TheString = ""
    TheDashes = "------------------------------"
    TheLineBreak = "\n"
    TheTab = "\t"
    #TheText = "your total is $"
    #TheNiteText = "nite special! your total is $"
    TheMinutes = 30
    TheRate = 0
    TheNiteFlag = False
    TheFee = ""
    i = 8

    TheString = "Price Chart:" + TheLineBreak
    TheString = TheString + TheDashes + TheLineBreak
    while i < 23:
        TheRate = get_rate(i, TheMinutes, day, is_holiday)
        TheNiteFlag = check_nite(i, TheMinutes, day)
        TheFee = get_fee(TheRate,num_games, num_people, day, TheNiteFlag, is_holiday)

        TheString = TheString + str(i) + ":" + str(TheMinutes) + TheTab + str(TheFee) + TheLineBreak

        #if(i < 21):
        #    TheString = TheString + str(i) + ":" + str(TheMinutes) + TheTab + TheText + str(TheFee) + TheLineBreak
        #else:
        #    TheString = TheString + str(i) + ":" + str(TheMinutes) + TheTab + TheNiteText + str(TheFee) + TheLineBreak
        #TheString = TheString + str(i) + ":" + str(TheMinutes) + TheTab + str(TheRate) + TheLineBreak
        if(i == 17 or i == 20):
            TheString = TheString + TheDashes + TheLineBreak
        i = i + 1

    return TheString

print(price_chart(4, 2, 1, False))
#print(price_chart(3, 2, 6, True))
#print(price_chart(4, 4, 7, False))
#print(price_chart(2, 1, 5, False))
#print(price_chart(2, 5, 2, True))

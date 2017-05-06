board = [[2,4,None,None],[1,2,3,3],[3,1,None,5],[4,3,None,None]]
board0 = [[3,None,2],[2,3,None],[None,2,None]]
board1 = [[1,2,3], [3,1,2], [2,3,1]]
board2 = [[2,4,None,None ], [1,2,3,4], [3,1,None,None ], [4,3,None,None ]]
board3 = [[2,4,1,3 ],[1,2,3,4 ],[3,1,4,2 ],[4,3,2,1 ]]
board4 = [[3,2,1],[2,3,1],[1,2,3]]
board5 = [[2,4,None,None],[1,2,3,3],[3,1,None,5],[4,3,1,2]]
board6 = [[2,1,None,None],[None,2,3,3],[3,1,None,5],[4,3,None,None]]
boardA = [[2,1,None,None],[None,2,3,3],[3,1,None,5],[4,3,None,None]]

board_1 = [[3,1,2],[2,3,1],[1,2,3]]
board_2 = [[3,1,2],[2,2,1],[1,2,3]]

cages1 = [['x', 6, [(0,0),(1,0)]], ['-', 1, [(0,1),(0,2)]], ['-', 1, [(2,0),(2,1)]], ['+', 7, [(1,1),(1,2),(2,2)]]]
cages2 = [['-', 2,[(0,0),(1,0)]], ['-', 2,[(2,0),(3,0)]], ['-', 2,[(1,1),(2,1)]], ['-', 2,[(0,3),(1,3)]], ['-', 1,[(0,1),(0,2)]], ['+',10,[(1,2),(2,2),(2,3)]], ['+', 9,[(3,1),(3,2),(3,3)]]]

TestBoard = [[1,2,3],[None,3,1],[3,2,1]]

def make_empty_board(n):
    x = 0
    y = 0
    #n = 3
    mylist = []

    #aa1 = 0
    #aa2 = 0

    while x < n:
        mylist.append([])
        while y < n:
            mylist[x].append(None)
            y = y + 1
        x = x + 1
        y = 0

    #bool1 = aa1 >= 0 and x <= 59
    return mylist

#region make_empty_board
#print(make_empty_board(2))
#endregion

def aa_make_board(n):
    matrix = n*[n*[None]]
    return matrix

#region aa_make_board
#print(aa_make_board(2))
#endregion

def is_valid_location(loc, puzzle):
    b = True
    newlist = puzzle
    tup = loc
    (x,y) = tup
    #print(x)
    #print(y)
    NumRows = len(puzzle)
    NumCols = len(puzzle[0])
    #print(NumRows)
    #print(NumCols)
    if x < 0 or y < 0:
        b = False
    else:        
        if x < NumRows and y < NumCols:
            b = True
        else:
            b = False
    
    return b

    #if (x >= 0 and y >= 0):
    #    try:
    #        newlist[x][y]
    #        b = True
    #    except :
    #        b = False
    #    return b
    #else:
    #    return b

#region is_valid_location
#print(is_valid_location((4,1), [[1,2], [2,1]]))
#print(is_valid_location((0,0), [[None]]))
#print(is_valid_location((1,1), [[None]]))
#print(is_valid_location((-1,1), board0))
#print(is_valid_location((1,2),board0))
#print(is_valid_location((0,0), board0))
#endregion

def is_complete(puzzle):
    item = None
    IsComplete = True

    for x in puzzle:
        if item in x:
            IsComplete = False
            #break
    
    return IsComplete

#region is_complete
#print(is_complete([[1,2,3],[3,4,2],[2,3,None]]))
#endregion

def get_value_at_location(puzzle, loc):
    tup = loc
    (x,y) = tup

    return puzzle[x][y]        

#region get_value_at_location
print(get_value_at_location([[1,2],[2,1]], (1,1)))
#print(get_value_at_location([[1,2],[None,1]], (1,0)))
#endregion    

def set_location(puzzle, value, loc):
    GoodToGo = False
    IsValidLocation = is_valid_location(loc, puzzle)
    IsComplete = is_complete(puzzle)
    
    if (IsValidLocation and not IsComplete):
        IsEmpty = get_value_at_location(puzzle, loc)
        if IsEmpty == None:
            GoodToGo = True
            newlist = puzzle
            tup = loc
            (x,y) = tup
            newlist[x][y] = value
    
    return GoodToGo

#region set_location
#print(set_location([[1]], 1, (0,0)))
#print(set_location([[1]], 1, (0,0)))
#print(set_location([[None]], 1, (0,0)))
#print(set_location([[None]], 1, (1,0)))
#print(set_location([[None]], 3, (0,0)))
#print(set_location([[1,2],[None,1]], 2, (1,0)))
#print(set_location([[3,None,2], [2,3,None], [None,2,None]], 1, (0,4)))
#print(set_location([[3,None,2], [2,3,None], [None,2,None]], 1, (0,0)))
#endregion

def unset_location(puzzle, loc):
    HasChanged = False
    IsValidLocation = is_valid_location(loc, puzzle)
    if IsValidLocation:
        IsEmpty = get_value_at_location(puzzle, loc)
        if (IsEmpty != None and IsValidLocation):
            tup = loc
            (x,y) = tup
            puzzle[x][y] = None
            HasChanged = True
    
    return HasChanged

#region unset_location
#print(unset_location([[1]], (0,0)))
#print(unset_location([[1]], (0,1)))
#print(unset_location([[None]], (0,0)))
#print(unset_location([[1,2],[1,1]], (1,0)))
#endregion

def get_size(puzzle):
    NumRows = len(puzzle)
    #NumCols = len(puzzle[0])
    return NumRows

#region get_size
#print(get_size([[None,None],[None,None]]))
#print(get_size([[1,2,3],[2,1,3],[None,None,3]]))
#print(get_size([[5]]))
#endregion

def get_valid_numbers(size):
    x = 0
    mylist = []
    while x < size:
        x = x + 1
        mylist.append(x)
    return mylist

#region get_valid_numbers
#print(get_valid_numbers(2))
#print(get_valid_numbers(1))
#print(get_valid_numbers(3))
#print(get_valid_numbers(4))
#print(get_valid_numbers(9))
#endregion

def contains_only_valid_symbols(puzzle, complete):
    Passed = True
    z = 0
    if complete:
        for x in puzzle:
            if Passed:
                for y in x:
                    if y == None:
                        Passed = False
                        break
            else:
                break
        if Passed:
            VaildNums = get_valid_numbers(len(puzzle))
            for w in puzzle:
                if Passed:
                    for z in w:
                        if z in VaildNums:
                            Passed = True
                        else:
                            Passed = False
                            break
                else:
                    break
    else:
        VaildNums = get_valid_numbers(len(puzzle))
        for w in puzzle:
            if Passed:
                for z in w:
                    if z in VaildNums or z == None:
                        Passed = True
                    else:
                        Passed = False
                        break
            else:
                break
    return Passed

#region contains_only_valid_symbols
#print(contains_only_valid_symbols(board0, False))
#print(contains_only_valid_symbols(board0, True))
#print(contains_only_valid_symbols([[1,1],[1,1]], True))
#print(contains_only_valid_symbols([[4]], True))

#print(contains_only_valid_symbols(board0(),False)) #True
#print(contains_only_valid_symbols(board0(),True)) # False
#print(contains_only_valid_symbols([[1,2],[3,4]],True)) # False
#print(contains_only_valid_symbols([[1,2],[2,-1]],True)) # False
#print(contains_only_valid_symbols(board3,True)) # True
#print(contains_only_valid_symbols(board6, False)) # False
#endregion

def has_repeat(xs, v):
    Hits = 0
    for x in xs:
        if (x == v and x != None):
            Hits = Hits + 1
    if Hits > 1:
        return True
    else:
        return False

#region has_repeat
#print(has_repeat([1,2,3], 1))
#print(has_repeat([1,2,1], 1))
#print(has_repeat([None], 1))
#print(has_repeat([None],1))
#print(has_repeat([2,1,3],1))
#print(has_repeat([1,2,1],1))
#print(has_repeat([1,None,3],1))
#print(has_repeat([1,None,3,1,2,4,5,6,7,8,9],3))
#endregion

def get_row(puzzle, row_index):
    NumRows = len(puzzle)
    if row_index <= NumRows - 1 and row_index >= 0:
        TheRow = puzzle[row_index]
    else:
        TheRow = None
    return TheRow

#region get_row
#print(get_row([[1,None],[2,None]], 0))
#print(get_row([[1,None],[2,None]], 1))
#print(get_row([[1,None],[2,None]], 2))
#print(get_row(board0,-2)) # None
#endregion

def is_valid_row(puzzle, row_index, complete):
    PassesTests = True
    IsUnique = True
    IsComplete = True
    TheRow = get_row(puzzle, row_index)
    if TheRow == None:
        PassesTests = False
    else:
        if not complete: # incomplete puzzle
            for x in TheRow:
                Repeats = has_repeat(TheRow,x)
            if Repeats:
                IsUnique = False
                PassesTests = False
            if IsUnique:
                VaildNums = get_valid_numbers(get_size(TheRow))
                for y in TheRow:
                    if y not in VaildNums and y != None:
                        PassesTests = False
                        break
                    else:
                        PassesTests = True
        else: # complete puzzle
            for x in TheRow:
                if x == None:
                    PassesTests = False
                    break
                else:
                    Repeats = has_repeat(TheRow,x)
                    if Repeats:
                        IsUnique = False
                        PassesTests = False
                    if IsUnique:
                        VaildNums = get_valid_numbers(get_size(TheRow))
                        if x in VaildNums:
                            PassesTests = True
                        else:
                            PassesTests = False
    return PassesTests

#region is_valid_row
#print(is_valid_row(board, 0, False))
#print(is_valid_row(board, 0, True))
#print(is_valid_row(board, 1, True))
#print(is_valid_row(board, 2, False))
#print(is_valid_row(board, -2, True))

#print(is_valid_row(board5,2,False))
#print(is_valid_row(board5,0,False))
#print(is_valid_row(board5,7,True))
#print(is_valid_row(board5,3,True))
#endregion

def has_valid_rows(puzzle, complete):
    PuzzleLength = len(puzzle)
    IsValidRow = True
    PassesTests = True
    x = 0
    while x < PuzzleLength:
        TheRow = get_row(puzzle, x)
        IsValidRow = is_valid_row(puzzle, x, complete)
        if IsValidRow:
            x = x + 1
        else:
            PassesTests = False
            break
    return PassesTests

#region has_valid_rows
#print(has_valid_rows(board0, False)) #True
#print(has_valid_rows(board0, True)) #False
#print(has_valid_rows(board3, True)) #True
#print(has_valid_rows(board5, False)) #False
#print(has_valid_rows([[1,2,3],[2,1,3],[3,1,3]], True)) # False - repeat
#endregion

def get_column(puzzle, col_index):
    Cols = []
    if col_index >= 0 and col_index < len(puzzle):
        for x in puzzle:
            Cols.append(x[col_index])
        return Cols
    else:
        return None

#region get_column
#print(get_column([[1, None],[2, None]], 0))
#print(get_column([[1, None],[2, None]], 1))
#print(get_column([[1, None],[2, None]], 2))
#print(get_column(board0,0)) # [3,2,None]
#print(get_column(board0,1)) # [None,3,2]
#print(get_column(board0,-1)) # None
#print(get_column(board0,6)) # None
#endregion

def is_valid_col(puzzle, col_index, complete):
    PassesTest = True
    Repeats = False
    if complete:
        ValidNum = get_valid_numbers(len(puzzle))
        if col_index > len(puzzle) or col_index < 0:
            PassesTest = False
        else:
            GetColumn = get_column(puzzle, col_index)
            for y in GetColumn:
                if y != None:
                    if not Repeats:
                        Repeats = has_repeat(GetColumn, y)
                        if  y not in ValidNum:
                            PassesTest = False
                            break
                    else:
                        PassesTest = False
                else:
                    PassesTest = False
                    break
    else: # not complete puzzle
        ValidNum = get_valid_numbers(len(puzzle))
        GetColumn = get_column(puzzle, col_index)
        for y in GetColumn:
            if not Repeats:
                Repeats = has_repeat(GetColumn, y)
                if  y not in ValidNum and y != None:
                    PassesTest = False
                    break
            else:
                PassesTest = False
    return PassesTest

#region is_valid_col
#print(is_valid_col(TestBoard,0,False)) # False

#print(is_valid_col(boardA, 0, False))
#print(is_valid_col(boardA, 0, True))
#print(is_valid_col(boardA, 1, True))
#print(is_valid_col(boardA, 3, False))
#print(is_valid_col(boardA, 7, True))

#print(is_valid_col([[None,1],[1,2]],0,False)) # True
#print(is_valid_col([[None,1],[1,2]],0,True)) # False
#print(is_valid_col(board6,1,True)) # False
#print(is_valid_col(board6,3,False)) # False
#print(is_valid_col(board6,-2,True)) # False
#print(is_valid_col(board3,2,True)) # True
#endregion

def has_valid_cols(puzzle, complete):
    PassesTests = True
    IsValidCol = True
    x = 0
    y = 0
    while x < len(puzzle):
        IsValidCol = is_valid_col(puzzle, x, complete)
        if not IsValidCol:
            PassesTests = False
            break
        x = x + 1
    return PassesTests

#region has_valid_cols

#print(has_valid_cols([[1,2],[2,1]], True))

#print(has_valid_cols([[1,2],[1,1]], True))
#print(has_valid_cols([[1,None],[2,1]], False))
#print(has_valid_cols([[1,None],[2,1]], True))
#print(has_valid_cols([[1,4],[2,1]], True))

#print(has_valid_cols(board0, False)) # True
#print(has_valid_cols(board0, True)) # False
#print(has_valid_cols(board3, True)) # True
#print(has_valid_cols(board6, False)) # False
#print(has_valid_cols(board4, True)) # False

#endregion

def is_valid_cage_solution(puzzle, op, expected_total, locations):
    PassesTest = True
    TempList = []
    tot = 0
    if op == "x":
        tot = 1
    for x in locations:
        tup = x
        (x,y) = tup
        TempList.append(puzzle[x][y])
    for item in TempList:
        if op == "+":
            tot = tot + item
        elif op == "-":
            tot = tot - item
            if tot < 0:
                tot = tot * -1
        elif op == "x":
            tot = tot * item
    if tot < 0:
        tot = tot * -1
    if tot != expected_total:
        PassesTest = False
    
    return PassesTest

#region is_valid_cage_solution
#print(is_valid_cage_solution([[1]], '+', 1, [(0,0)]))
#print(is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(0,0),(1,0)]))
#print(is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(1,0),(0,0)]))
#print(is_valid_cage_solution([[1,2],[2,1]], 'x', 4, [(0,0),(0,1),(1,0),(1,1)]))
#print(is_valid_cage_solution([[1,1],[1,1]], 'x', 1, [(0,0)]))
#print(is_valid_cage_solution([[1,2],[2,1]], '+', 4, [(0,0),(0,1)]))

#print(is_valid_cage_solution([[1]], '+', 1, [(0,0)])) # True
#print(is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(0,0),(1,0)])) # True)
#print(is_valid_cage_solution([[1,2],[2,1]], '-', 1, [(1,0),(0,0)])) # True
#print(is_valid_cage_solution([[1,2],[2,1]], 'x', 4, [(0,0),(0,1),(1,0),(1,1)])) # True
#print(is_valid_cage_solution([[1,2],[2,1]], '+', 4, [(0,0),(0,1)])) # False
#print(is_valid_cage_solution(board1, '-', 5, [(0,0),(0,1)])) # False
#print(is_valid_cage_solution(board3, 'x', 6, [(1,1),(1,2),(1,3)])) # False
#endregion

def is_valid(puzzle, cages, complete):
    PassesTests = True
    HasValidRows = True
    HasValidCols = True
    IsValidCage = True
    x = 0
    idx1 = 0
    if complete:
        HasValidRows = has_valid_rows(puzzle, complete)
        if HasValidRows:
            HasValidCols = has_valid_cols(puzzle, complete)
            if HasValidCols:
                if cages:
                    for x in cages:
                        op = cages[idx1][0]
                        ex = cages[idx1][1]
                        loc = cages[idx1][2]
                        IsValidCage = is_valid_cage_solution(puzzle, op, ex, loc)
                        idx1 = idx1 + 1
                        if not IsValidCage:
                            PassesTests = False
                else:
                    PassesTests = True
            else: 
                PassesTests = False
        else:
            PassesTests = False
    else: # incomplete puzzle
        HasValidRows = has_valid_rows(puzzle, complete)
        if HasValidRows:
            HasValidCols = has_valid_cols(puzzle, complete)
            if not HasValidCols:
                PassesTests = False
        else:
            PassesTests = False
    return PassesTests

#region is_valid

#print(is_valid(board_1, [], True)) # False

#print(is_valid(board_1, [], False)) # True
#print(is_valid(board_1, [['+',5,[(0,0),(1,0)]]], True)) #True
#print(is_valid(board_1, [['+',4,[(0,0),(1,0)]]], True)) # False
#print(is_valid(board_2, [['+',5,[(0,0),(1,0)]]], True)) # False
#print(is_valid([[None, None],[None,None]], [['+',5,[(0,0),(1,0)]]], False)) # True

#print(is_valid(board0,[],False)) # True
#print(is_valid(board1,[],True)) # True
#print(is_valid(board4,[],True)) # False
#print(is_valid(board5,[],False)) # False
#print(is_valid(board1,[['+',4,[(0,0),(1,0)]],['x',3,[(0,2),(1,2),(2,2)]]],True)) # False
#print(is_valid(board1,[['+',4,[(0,0),(1,0)]],['x',6,[(0,2),(1,2),(2,2)]]],True)) # True
#print(is_valid(board2,[['+',5,[(0,0),(1,0)]],['x',6,[(0,0),(1,0),(2,0)]]],False)) # True
#print(is_valid(board4,cages1,True)) # True
#print(is_valid([[4,2,1,3],[2,3,4,1],[3,1,2,4],[1,4,3,2]],cages2,True)) # True
#endregion

def get_board_string(puzzle):
    index = 0
    a = 0
    TheString = ""
    spaces = "     "
    Line1 = "[0] [1] [2]\n"
    Dashes = "-----------\n"
    Pipe = " | "
    ColLength = len(puzzle)
    while a < len(puzzle):
        print("[" + str(a) + "]", end=' ')
        a = a + 1

    #for x in puzzle:
    #    for y in x:
    #        print(index, y)
    #        index = index + 1 

    #for x in puzzle:
    #    for y in x:
    #        TheString = spaces + Line1 + spaces  + Dashes + "[0]" + Pipe + "3" + Pipe + "1" + Pipe + "2" + Pipe + "\n[1]" + Pipe + "2" + Pipe + "." + Pipe + "." + Pipe + "\n[2]" + Pipe + "." + Pipe + "." + Pipe + "." + Pipe + "\n" + spaces  + Dashes
    return TheString

#print(get_board_string([[3,1,2],[2,None,None],[None,None,None]]))

def get_missing_numbers_row_or_col(xs):
    a = 1
    MissingVals = []
    #VaildNumbers = get_valid_numbers(len(xs))
    while a <= len(xs):
        if a not in xs:
            MissingVals.append(a)
        a = a + 1
    return MissingVals

#region get_missing_numbers_row_or_col
#print(get_missing_numbers_row_or_col([1,2]))

#print(get_missing_numbers_row_or_col([1,2])) # []
#print(get_missing_numbers_row_or_col([1,None,2])) # [3]
#print(get_missing_numbers_row_or_col([None,None,None])) # ,[1,2,3])
#print(get_missing_numbers_row_or_col([None,None,1])) #,[2,3])
#print(get_missing_numbers_row_or_col([1,1,1])) #,[2,3])


#endregion

def candidates_at_location(puzzle, loc):
    PassesTests = True
    MyList = []
    IsValidLoc = is_valid_location(loc, puzzle)
    if IsValidLoc:
            MyList = get_missing_numbers_row_or_col(puzzle)
    else:
        PassesTests = False

    x = 5432

    if not PassesTests:
        return None
    else:
        return MyList

#region candidates_at_location

#print(candidates_at_location([[1]], (0,0)))

#print(candidates_at_location([[None]], (0,0))) # ,[1]
#print()
#endregion

####################################
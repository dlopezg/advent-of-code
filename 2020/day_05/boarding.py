def readBoardingpasses(file):
    return [x.strip() for x in open(file).readlines()]

def splitList(listToSplit):
    a = listToSplit[:len(listToSplit)//2]
    b = listToSplit[len(listToSplit)//2:]
    return a, b

def checkMissingSeat(seatList):
    completeList = list(range(min(seatList),max(seatList)))
    for seatID in completeList:
        if seatID not in seatList:
            return seatID

def calculateSeat(boardingpasses):
    seatID = list()
    for boardingpass in boardingpasses:
        rows = boardingpass[:7]
        cols = boardingpass[7:]
        seatRowList = list(range(128))
        seatColList = list(range(8))

        for row in rows:
            lower, upper = splitList(seatRowList)
            seatRowList = lower if row == 'F' else upper
        
        for col in cols:
            lower, upper = splitList(seatColList)
            seatColList = lower if col == 'L' else upper

        seatID.append(int(seatRowList[0]) * 8 + int(seatColList[0]))
    return seatID

# Problem 1:
boardingpasses = readBoardingpasses('boarding.txt')
seatIDs = calculateSeat(boardingpasses)
print(max(seatIDs))

#Problem 2:
print(checkMissingSeat(seatIDs))

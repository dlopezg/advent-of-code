def readNearbyTickets(file):
    lines = [line.strip().split(',') for line in open(file).readlines()]
    nearbyTickets = list()
    for line in lines:
        line = [int(number) for number in line]
        nearbyTickets.append(line)
    return nearbyTickets


def readValidRanges(file):
    rules = {}
    fieldNames = list()
    lines = [line.strip().split(': ') for line in open(file).readlines()]
    for line in lines:
        ranges = line[1].replace(' or ', ' ').replace('-', ' ')
        ranges = [int(number) for number in ranges.split(' ')]
        valid = list(range(ranges[0], ranges[1] + 1)) + \
            list(range(ranges[2], ranges[3]+1))
        rules[line[0]] = valid
        fieldNames.append(line[0])
    return (rules, fieldNames)


def findInvalidNumbers(nearbyTickets, validRanges):
    valid = list()
    for item in validRanges:
        valid += validRanges[item]
    error = 0
    for ticket in nearbyTickets:
        for number in ticket:
            if number not in valid:
                error += number
    return error


def discardInvalidTickets(nearbyTickets, validRanges):
    validTickets = list()
    valid = list()
    for item in validRanges:
        valid += validRanges[item]
    for ticket in nearbyTickets:
        validTicket = True
        for number in ticket:
            if number not in valid:
                validTicket = False
        if validTicket:
            validTickets.append(ticket)
    return validTickets


def searchPosibilities(posibleValid):
    posibilities = list()
    result = list()
    for item in posibleValid:
        result.append((len(posibleValid[item]), item, posibleValid[item]))
        posibilities.append(posibleValid[item])
    result.sort()
    for i in range(1, len(result)):
        target = result[i-1][2][0]
        for j in range(i, len(result)):
            if target in result[j][2]:
                result[j][2].remove(target)
    return result


def myTicket(decodedFields, ticket):
    res = 1
    for field in decodedFields:
        if field[1].startswith('departure'):
            res *= ticket[field[2][0]]
    return res


def decodeTicket(nearbyTickets, validRanges, ticket):
    decodedFields = {}
    validTickets = discardInvalidTickets(nearbyTickets, validRanges)
    for field in validRanges:
        decodedFields[field] = list()
        for position in range(len(validRanges)):
            validField = True
            for ticket_ in validTickets:
                if ticket_[position] not in validRanges[field]:
                    validField = False
                    break
            if validField:
                validList = decodedFields[field]
                validList.append(position)
                decodedFields[field] = validList
    return myTicket(searchPosibilities(decodedFields), ticket)


ticket = [109, 137, 131, 157, 191, 103, 127, 53, 107,
          151, 61, 59, 139, 83, 101, 149, 89, 193, 113, 97]
nearbyTickets = readNearbyTickets('nearbyTickets.txt')
validRanges, fieldNames = readValidRanges('valid.txt')
# Part 1: Find invalid numbers:
invalidNumbers = findInvalidNumbers(nearbyTickets, validRanges)
# Part 2:
print(decodeTicket(nearbyTickets, validRanges, ticket))

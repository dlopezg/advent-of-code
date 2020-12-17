from pprint import pprint
from copy import deepcopy


def readLines(file):
    data = open(file).read().split('\n')
    timestamp = int(data[0])
    ids = [int(busId) for busId in data[1].split(',') if busId != 'x']
    return (timestamp, ids)


def departures(buses):
    timestamp, ids = buses
    busIds = deepcopy(ids)
    for idx, busId in enumerate(ids):
        while busIds[idx] <= timestamp:
            busIds[idx] += busId
        busIds[idx] -= timestamp
    return min(busIds) * ids[busIds.index(min(busIds))]


def departures_(data):
    timestamp, idList = data
    found = False
    waitTime = 0
    while found == False:
        waitTime += 1
        for busId in idList:
            if (timestamp + waitTime) % busId == 0:
                found = True
                break
    return waitTime * busId


pprint(departures_(readLines('bus.txt')))

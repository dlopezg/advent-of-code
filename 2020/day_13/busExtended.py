from pprint import pprint
from copy import deepcopy
from math import gcd


def readLines(file):
    lines = [line for line in open(file).readlines()]
    busIds = lines[1].split(',')
    ids = list()
    for idx, busid in enumerate(busIds):
        if busid != 'x':
            ids.append([int(busid), idx])
    return ids


def simulateBruteForce(data):
    ids = [busId[0] for busId in data]
    idxs = [busId[1] for busId in data]

    timestamp = ids[0]
    step = ids[0]
    res = [0] * (len(idxs) - 1)
    while True:
        for i, idx in enumerate(idxs[1:]):
            reminder = (timestamp + idx) % ids[i+1]
            if reminder:
                break
            else:
                res[i] = True
        timestamp += step
        if all(res):
            break
    return timestamp - step

# The main idea here is to found the timestamp when the first
# bus match the condition. This match occurs again and again every
# T seconds, where T is the bus ID.
# Therefore, we do not need to check every minute looking for the
# second match.
# When the second match occurs, we need to find the new value of T that should
# be added to the timestamp. This value will be the Least Common Multiple
# of the two elements of the list.


def simulateLCM(data):
    timestamp = 0
    step = 1
    data.sort()
    busses = [busId[0] for busId in data]
    offset = [busId[1] for busId in data]
    found = False
    matches = 0
    while matches < len(busses):
        while not found:
            found = False
            for idx in range(0, matches + 1):
                found = False
                if (timestamp + offset[idx]) % busses[idx] != 0:
                    break
                found = True
            if found:
                step = leastCommonMultiple(busses[:idx + 1])
                found = False
                matches += 1
                break
            timestamp += step
    return timestamp


def leastCommonMultiple(values):
    if len(values) == 1:
        return values[0]
    lcm = values[0]
    for value in values[1:]:
        lcm = lcm * value // gcd(lcm, value)
    return lcm


pprint(simulateLCM(readLines('bus.txt')))

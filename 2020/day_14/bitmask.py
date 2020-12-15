from pprint import pprint
import itertools


def parseInput(file):
    lines = [line.strip() for line in open(file).readlines()]
    memoryList = list()
    maskList = list()
    mask = str()
    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
            continue
        line = line.replace('mem[', '')
        line = line.replace(']', '')
        line = line.split(' = ')
        maskList.append(mask)
        memoryList.append((int(line[0]), int(line[1])))
    return (memoryList, maskList)


def applyBitMask(value, mask):
    masked = str()
    for i in range(len(value)):
        if mask[i] in ['0', '1']:
            masked += mask[i]
            continue
        masked += value[i]
    return binToint(masked)


def binToint(value):
    return int(value, 2)


def intTobin(value):
    return bin(value)[2:].zfill(36)


def initializeDockingProgram(memoryList, maskList):
    memory = {}
    result = 0
    for idx, instruction in enumerate(memoryList):
        address, value = instruction
        value = intTobin(value)
        memory[address] = applyBitMask(value, maskList[idx])
    for key in memory:
        result += memory[key]
    return result


def initializeDockingProgramV2(memoryList, maskList):
    memory = {}
    result = 0
    for idx, instruction in enumerate(memoryList):
        address, value = instruction
        addressList = applyBitMaskV2(intTobin(address), maskList[idx])
        for address in addressList:
            memory[address] = value
    for key in memory:
        result += memory[key]
    return result


def applyBitMaskV2(address, mask):
    addressList = list()
    masked = str()
    counter = 0
    for i in range(len(mask)):
        if mask[i] in ['1', 'X']:
            masked += mask[i]
            counter += mask[i] == 'X'
            continue
        masked += address[i]

    # The number of memory address conbinations is 2^number_of_x
    # Using itertool product we can compute each combination for x bits.
    combinations = itertools.product(('1', '0'), repeat=counter)

    for combination in combinations:
        address = str()
        pointer = 0
        for i in masked:
            if i != 'X':
                address += i
                continue
            address += combination[pointer]
            pointer += 1
        addressList.append(address)
    return addressList


memoryList, maskList = parseInput('bitmask.txt')
# print(initializeDockingProgram(memoryList, maskList))
print(initializeDockingProgramV2(memoryList, maskList))

def readLines(file):
    lines = [line.strip() for line in open(file).readlines()]
    maths = list()
    for line in lines:
        line = line.replace('(', '( ')
        line = line.replace(')', ' )')
        line = line.split()
        maths.append(line)
    return maths


def operate(val, val_, operator):
    if operator == '+':
        return val + val_
    return val * val_


def parentheses(line):
    mainPointer = 0
    while True:
        toeval = line[mainPointer]
        if toeval == '(':
            openPointer = mainPointer + 1
        if toeval == ')':
            line[openPointer - 1] = operations(line[openPointer: mainPointer])
            del line[openPointer: mainPointer + 1]
            mainPointer = 0
            continue
        mainPointer += 1
        if mainPointer == len(line):
            return line


def operations(line):
    for operator in ['+', '*']:
        mainPointer = 0
        while True:
            toeval = line[mainPointer]
            if toeval == operator:
                val = int(line[mainPointer - 1])
                val_ = int(line[mainPointer + 1])
                res = operate(val, val_, toeval)
                line[mainPointer - 1] = res
                del line[mainPointer: mainPointer + 2]
                mainPointer = 0
                continue
            mainPointer += 1
            if mainPointer == len(line):
                break
    return line[0]


def compute(maths):
    res = 0
    for line in maths:
        line = parentheses(line)
        res += operations(line)
    print(res)


maths = readLines('maths.txt')
compute(maths)

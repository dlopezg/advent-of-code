def readNumber(file):
    return [int(num.strip()) for num in open(file).readlines()]

def findSum(target,preamble):
    for idx,num in enumerate(preamble):
        for _,num_ in enumerate(preamble[idx + 1:]):
            if num + num_ == target:
                return True
    return False

def findContiguous(target,xmasCode):
    for idx,num in enumerate(xmasCode):
        accumulator = num
        contiguousList = list()
        contiguousList.append(num)
        for _,num_ in enumerate(xmasCode[idx + 1:]):
            contiguousList.append(num_)
            accumulator += num_
            if accumulator > target:
                break
            if accumulator == target:
                return min(contiguousList) + max(contiguousList)
    return False
    
def inspectXMAS(xmasCode):
    preambleLenght = 25
    for i in range(preambleLenght,len(xmasCode)):
        target = xmasCode[i]
        preamble = xmasCode[i - preambleLenght : i]
        found = findSum(target,preamble)
        if found:
            continue
        else:
            contiguous = findContiguous(target,xmasCode)
            return target,contiguous
        
print(inspectXMAS(readNumber('xmas.txt')))
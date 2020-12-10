from functools import lru_cache 

def readLines (file):
    return [int(x.strip()) for x in open(file).readlines()]

def joltage(adaptersJoltageList):
    joltageOffset = {}
    for idx,adapter in enumerate(adaptersJoltageList):
        if idx == len(adaptersJoltageList) - 1:
            break
        offset = adaptersJoltageList[idx+1] - adapter
        joltageOffset[offset] = 1 if offset not in joltageOffset else joltageOffset[offset] + 1
    
    return joltageOffset

def combinations (joltageList):
    # The main idea here is to build a tree. 
    tree = {} 
    idx = 0
    while idx < len(joltageList):
        node = joltageList[idx]
        childNodes = list()
        # find posible child nodes:
        idx_ = idx + 1
        while idx_ < len(joltageList):
            if joltageList[idx_] - joltageList[idx] <= 3:
                childNodes.append(joltageList[idx_])
                idx_ += 1
            else:
                break
        tree[node] = childNodes
        idx += 1
    print(tree)
    return tree

def DFS(tree,seed):
    combinations = 0
    childNodes = tree[seed]
    if not childNodes:
        return int(1)
    else:
        for node in childNodes:
            combinations += DFS(tree,node)
    return combinations

# Explanation: For each index, we need to figure out all the possible ways 
# to reach the final of the list. If we reach the final of the list, we 
# add 1 to the final counter. The function lru_cache is required for memoization:
# For a given input (index) the output of the function is stored and we don't need
# to compute the function again for that index.
# Using the recursive call to dypro function and the implementation of lru_cache 
# we can solve the problem almost inmediately. 
@lru_cache(None)
def dypro(idx):
    counter = 0
    idx_ = idx + 1
    if idx == len(joltageList) - 1:
        return 1
    while idx_ < len(joltageList) and joltageList[idx_] - joltageList[idx] <= 3:
        counter += dypro(idx_)
        idx_ += 1
    return counter

# Parse input:
joltageList = readLines('joltage.txt')
chargingOutlet = 0
device = max(joltageList) + 3
joltageList.append(device)
joltageList.append(chargingOutlet)
joltageList.sort()

# Part 1 - Joltage steps:
# result = joltage(joltageList)
# print(result[1]*result[3])

# Part 2 - DFS + tree (VERY slow):
# dic = combinations(joltageList)
# result = DFS(dic,chargingOutlet)
# print(result)

# Better option: dynamic programming:
result = dypro(0)
print(result)    
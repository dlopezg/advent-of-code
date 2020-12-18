from pprint import pprint
from copy import deepcopy


def readLines(file):
    return [list(line.strip()) for line in open(file).readlines()]


def initialize(initialState):
    cubes = {}
    l = len(initialState)
    for x in range(-20 + l // 2, 20 + l // 2):
        for y in range(-20 + l // 2, 20 + l // 2):
            for z in range(-7, 7):
                for w in range(-7, 7):
                    if z == 0 and w == 0 and (0 <= x < l) and (0 <= y < l):
                        cubes[(x, y, z, w)] = initialState[x][y]
                    else:
                        cubes[(x, y, z, w)] = '.'
    return cubes


def cycle(cubes, nCycles):
    for _ in range(nCycles):
        active = 0
        cubes_ = deepcopy(cubes)
        for cube in cubes:
            activeNeighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        for l in [-1, 0, 1]:
                            if not (i == 0 and j == 0 and k == 0 and l == 0):
                                cube_ = (cube[0] + i, cube[1] + j,
                                         cube[2] + k, cube[3] + l)
                                if cube_ in cubes and cubes[cube_] == '#':
                                    activeNeighbors += 1
            if cubes_[cube] == '#':
                if activeNeighbors in [2, 3]:
                    active += 1
                else:
                    cubes_[cube] = '.'
            elif cubes_[cube] == '.':
                if activeNeighbors == 3:
                    cubes_[cube] = '#'
                    active += 1
        cubes = deepcopy(cubes_)
        print('CYCLE COMPLETE')
    return active


initialState = readLines('cubes.txt')
cubes = initialize(initialState)
nCycles = 6
res = cycle(cubes, nCycles)
print(res)

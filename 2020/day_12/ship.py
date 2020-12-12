from pprint import pprint


def readLines(file):
    return[(line[0], int(line[1:].strip())) for line in open(file).readlines()]


def move(position, action):
    xcor, ycor, facing = position
    key, value = action

    if key == 'N' or (key == 'F' and facing == 'N'):
        ycor += value
    elif key == 'S' or (key == 'F' and facing == 'S'):
        ycor -= value
    elif key == 'E' or (key == 'F' and facing == 'E'):
        xcor += value
    elif key == 'W' or (key == 'F' and facing == 'W'):
        xcor -= value
    else:
        facing = rotate(key, value, facing)

    return xcor, ycor, facing


def rotate(key, value, facing):
    orientations = ['N', 'E', 'S', 'W']
    degrees = [0, 90, 180, 270]

    orientationIdx = orientations.index(facing)
    degreesIdx = degrees.index(value)

    if key == 'R':
        return orientations[(orientationIdx + degreesIdx) % len(orientations)]
    return orientations[orientationIdx - degreesIdx]


def movement(actionList):
    position = (0, 0, 'E')
    for action in actionList:
        position = move(position, action)
        print(position)
    return manhattan((0, 0), (position[0], position[1]))


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


actions = readLines('ship.txt')
result = movement(actions)
pprint(result)

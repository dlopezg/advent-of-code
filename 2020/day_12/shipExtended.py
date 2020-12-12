from pprint import pprint
import math


def readLines(file):
    return[(line[0], int(line[1:].strip())) for line in open(file).readlines()]


def move(position, waypoint, action):
    xcor, ycor, facing = position
    xcor_, ycor_ = waypoint
    xrel = xcor_ - xcor
    yrel = ycor_ - ycor
    key, value = action

    if key == 'N':
        ycor_ += value
    elif key == 'S':
        ycor_ -= value
    elif key == 'E':
        xcor_ += value
    elif key == 'W':
        xcor_ -= value
    elif key == 'F':
        xcor += xrel * value
        ycor += yrel * value
        xcor_ = xcor + xrel
        ycor_ = ycor + yrel
    else:
        shipPosition = (xcor, ycor)
        waypointPosition = (xcor_, ycor_)
        xcor_, ycor_ = rotateVector(action, shipPosition, waypointPosition)

    position = (xcor, ycor, facing)
    waypoint = (xcor_, ycor_)
    return position, waypoint


def rotateVector(action, shipPosition, waypointPosition):
    orientation, angle = action
    xcor, ycor = shipPosition
    xcor_, ycor_ = waypointPosition
    xrel = xcor_ - xcor
    yrel = ycor_ - ycor

    if orientation == 'R':
        angle = - angle

    angle = math.radians(angle)
    xcor_ = round(xrel * math.cos(angle) - yrel * math.sin(angle))
    ycor_ = round(xrel * math.sin(angle) + yrel * math.cos(angle))
    return (xcor + xcor_, ycor + ycor_)


def movement(actionList):
    position = (0, 0, 'E')
    waypoint = (10, 1)
    for action in actions:
        position, waypoint = move(position, waypoint, action)
        print(position)
    return manhattan((0, 0), (position[0], position[1]))


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


actions = readLines('ship.txt')
result = movement(actions)
pprint(result)

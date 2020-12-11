from pprint import pprint
import copy


def readLayout(file):
    return [list(line.strip()) for line in open(file).readlines()]


def checkAdjacent(position, layout):
    xcor, ycor = position
    xlen = len(layout) - 1
    ylen = len(layout[0]) - 1
    seat = layout[xcor][ycor]
    occupiedSeats = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                x = xcor + i
                y = ycor + j
                if 0 <= x <= xlen and 0 <= y <= ylen:
                    if layout[x][y] == '#':
                        occupiedSeats += 1

    if seat == 'L' and occupiedSeats == 0:
        return ('#', 1)
    if seat == '#' and occupiedSeats >= 4:
        return ('L', 1)
    return (seat, 0)


def checkVisible(position, layout):
    xcor, ycor = position
    xlen = len(layout) - 1
    ylen = len(layout[0]) - 1
    seat = layout[xcor][ycor]
    occupiedSeats = 0

    # Direction - down:
    for i in range(1, xlen - xcor + 1):
        seen = layout[xcor + i][ycor]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - up:
    for i in range(1, xcor + 1):
        seen = layout[xcor - i][ycor]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - left:
    for i in range(1, ycor + 1):
        seen = layout[xcor][ycor - i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - right:
    for i in range(1, ylen - ycor + 1):
        seen = layout[xcor][ycor + i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - down left:
    limit = min([xlen - xcor, ycor])
    for i in range(1, limit + 1):
        seen = layout[xcor + i][ycor - i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - up left:
    limit = min([xcor, ycor])
    for i in range(1, limit + 1):
        seen = layout[xcor - i][ycor - i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - up right:
    limit = min([xcor, ylen - ycor])
    for i in range(1, limit + 1):
        seen = layout[xcor - i][ycor + i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break
    # Direction - down right:
    limit = min([xlen - xcor, ylen - ycor])
    for i in range(1, limit + 1):
        seen = layout[xcor + i][ycor + i]
        if seen == '.':
            continue
        if seen == '#':
            occupiedSeats += 1
        break

    if seat == 'L' and occupiedSeats == 0:
        return ('#', 1)
    if seat == '#' and occupiedSeats >= 5:
        return ('L', 1)
    return (seat, 0)


def fillLayout(layout):
    while True:
        changed = 0
        newLayout = copy.deepcopy(layout)
        for idx, line in enumerate(layout):
            for idx_, _ in enumerate(line):
                newLayout[idx][idx_], change = checkVisible(
                    (idx, idx_), layout)
                changed += change
        layout = copy.deepcopy(newLayout)
        if changed == 0:
            break
    return sum([line.count('#') for line in layout])


layout = readLayout('layout.txt')
result = fillLayout(layout)
pprint(result)

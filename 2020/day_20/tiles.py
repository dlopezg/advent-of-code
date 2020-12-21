from pprint import pprint
import numpy


def parseInput(file):
    tileList = list()
    tiles = open(file).read().split('\n\n')
    tiles = [tile.split('\n') for tile in tiles]
    for tile in tiles:
        tileId = int(tile[0].replace('Tile ', '').replace(':', ''))
        tileList.append([tileId, tile[1:]])
    return tileList


def extractEdges(tiles):
    for tile in tiles:
        edge = list()
        edge.append(tile[1][0][::-1])
        edge.append(tile[1][-1][::-1])
        edge.append(''.join([line[0] for line in tile[1]][::-1]))
        edge.append(''.join([line[-1] for line in tile[1]][::-1]))
        edge.append(tile[1][0])
        edge.append(tile[1][-1])
        edge.append(''.join([line[0] for line in tile[1]]))
        edge.append(''.join([line[-1] for line in tile[1]]))
        tile.append(edge)
        # For the possible matches:
        tile.append([])
    return tiles


def matchingTiles(tile, tile_):
    edges, edges_ = tile[2], tile_[2]
    for i in range(len(edges)):
        for j in range(len(edges_)):
            if edges[i] == edges_[j]:
                return edges[i]
    return False


def findCorners(tiles):
    for i in range(len(tiles) - 1):
        for j in range(i + 1, len(tiles)):
            match = matchingTiles(tiles[i], tiles[j])
            if match:
                tiles[i][3].append(match)
                tiles[j][3].append(match)
    return numpy.prod([tile[0] for tile in tiles if len(tile[3]) == 2])


tiles = parseInput('tiles.txt')
tiles = extractEdges(tiles)
corners = findCorners(tiles)
print(corners)

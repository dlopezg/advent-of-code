from functools import reduce

def multiplyList(list_):
    return reduce(lambda x, y: x*y, list_)

def readMap(file):
    return [list(x.rstrip()) for x in open(file).readlines()]

def searchForTrees(map,slopes):
    nRow,nCol = len(map), len(map[0])
    right,down = slopes
    i,j=0,0
    counter = {
        '.' : 0,
        '#' : 0
    }
    while i < nRow:
        counter[map[i][j]] += 1
        i += down
        j = j + right - nCol if (j + right >= nCol) else j + right
            
    return counter

def tryDifferentSlopes (slopes):
    map = readMap('map.txt')
    paths = [searchForTrees(map,slope) for slope in slopes]
    return multiplyList([path['#'] for path in paths])
        
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
print(tryDifferentSlopes(slopes))
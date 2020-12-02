def readDatabase (filename):
    return [parseLine(line) for line in open(filename).readlines()]

def parseLine (line):
    tmp = line.rstrip().split()
    lo,hi = [int(x) for x in tmp[0].split('-')]
    character = tmp[1][0]
    pwd = tmp[2]
    return [lo,hi,character,pwd]

def findCorrectPwd (filename):
    counter = 0
    pwdDatabase = readDatabase(filename)
    for pwd in pwdDatabase:
        n = pwd[3].count(pwd[2])
        if pwd[0] <= n <= pwd[1]:
            counter += 1
    return counter

def findNewCorrectPwd (filename):
    counter = 0
    pwdDatabase = readDatabase(filename)
    for pwd in pwdDatabase:
        idx,idx_,cha,pw = pwd
        # XOR operator - Sets each bit to 1 if only one of two bits is 1:
        if (pw[idx-1] == cha) ^ (pw[idx_-1] == cha):
            counter += 1
    return counter

# Problem 1:
print(findCorrectPwd("pwd.txt"))
# Problem 2:
print(findNewCorrectPwd("pwd.txt"))
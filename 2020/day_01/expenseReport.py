def readIntLines (filename):
    return [int(x) for x in open(filename).readlines()]

def findSum (expenseReport):
    for idx, expense in enumerate(expenseReport):
        for idx_ in range(idx,len(expenseReport)):
            if expense + expenseReport[idx_] == 2020:
                return [expense,expenseReport[idx_]]
    return "Not found"

report = readIntLines("expenseReport.txt")
values = findSum(report)
print(values[0]*values[1]) 
    
def readIntLines (filename):
    return [int(x) for x in open(filename).readlines()]
    
def findValuesExtended(report):
    for idx, expense in enumerate(report):
        for idx_ in range(idx,len(report)):
            for idx__ in range(idx_,len(report)):
                if expense + report[idx_] + report[idx__]  == 2020:
                    return [expense,report[idx_],report[idx__]]
    return False

report = readIntLines("expenseReport.txt")
values = findValuesExtended(report)
print(values[0]*values[1]*values[2])
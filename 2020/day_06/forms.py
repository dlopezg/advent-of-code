def parseForms(file):
    lines = open(file).readlines()
    group = str()
    groups = list()
    for line in lines:
        line = line.strip()
        if line:
            group = group + line
            continue
        groups.append(group)
        group = str()
    groups.append(group)
    return groups

def findPositiveResponses(formList):
    counter = 0
    for form in formList:
        answered = {}
        for answer in form:
            if answer not in answered:
                answered[answer] = 1
                counter += 1
    return counter

formList = parseForms('forms.txt')
answered = findPositiveResponses(formList)
print(answered)


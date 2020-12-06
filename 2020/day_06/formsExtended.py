def parseForms(file):
    lines = open(file).readlines()
    group = list()
    groups = list()
    for line in lines:
        line = line.strip()
        if line:
            group.append(line)
            continue
        groups.append(group)
        group = list()
    groups.append(group)
    return groups

def findPositiveResponses(groups):
    counter = 0
    for group in groups:
        answers = {}
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers[answer] = 1
                    continue
                answers[answer] += 1
        for _, responses in answers.items():
            if responses == len(group):
                counter += 1
    return counter

formList = parseForms('forms.txt')
print(findPositiveResponses(formList))

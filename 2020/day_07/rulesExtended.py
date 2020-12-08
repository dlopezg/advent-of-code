import re

# The main idea here is to create a dictionary where 
# KEY: Is a node (color of the bag)
# VALUE: List of nodes (content of the parent bag)
# conected to parent node. 
# Using expand the graph using 'DFS'
def parseRules(file):
    # Read file input:
    lines = [line[:-2].strip() for line in open(file).readlines()]
    graph = {}
    for line in lines:
        # Split the original line using regular expressions and 
        # delete empty elements:
        line = line.replace('no other','')
        line = re.split(' contain |, | bags| bag',line)
        line = list(filter(None, line))

        # Generate the graph:
        parentNode,childNodeList = line[0],line[1:]
        childList = list()
        for childNode in childNodeList:
            childSplit = childNode.split(' ')
            childNodeNumber = int(childSplit[0])
            childNodeName = childSplit[1] + ' ' + childSplit[2]
            childList.append((childNodeName,childNodeNumber))
        if parentNode not in graph:
            graph[parentNode] = childList
    return graph

# Recursive implementation of Deep First Seach:
def DFS(graph,seed):
    counter = 1
    for (neighbour,n) in graph[seed]:
        counter += n * DFS(graph,neighbour)
    return counter    

graph = parseRules('rules.txt')
seed = 'shiny gold'
print(DFS(graph,seed)-1)
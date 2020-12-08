import re

# The main idea here is to create a dictionary where 
# KEY: Is a node (color)
# VALUE: Each parent of this node. 
# Using expand the graph using DFS (Deep First Search)
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
        for childNode in childNodeList:
            childSplit = childNode.split(' ')
            childNodeNumber = int(childSplit[0])
            childNodeName = childSplit[1] + ' ' + childSplit[2]
            if childNodeName in graph:
                graph[childNodeName].append(parentNode)
                continue
            graph[childNodeName] = [parentNode]
    return graph

# Recursive implementation of Deep First Seach:
def DFS(graph,visited,seed):
    if seed not in visited:
        visited.add(seed)
        if seed in graph:
            for neighbour in graph[seed]:
                DFS(graph,visited,neighbour)


visited = set()
seed = 'shiny gold'
graph = parseRules('rules.txt')
DFS(graph,visited,seed)
print(len(visited)-1)
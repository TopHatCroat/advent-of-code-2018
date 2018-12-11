import operator
from collections import defaultdict

def topological_sort(graph):
    in_degree = { e : 0 for e in graph }
    for edge in graph:
        for vertex in graph[edge]:
            in_degree[vertex] += 1

    q = list(filter(lambda x: in_degree[x] == 0, in_degree))
    path = []
    while q:
        edge = min(q)
        q.remove(edge)
        path.append(edge)
        for vertex in graph[edge]:
            in_degree[vertex] -= 1
            if in_degree[vertex] == 0:
                q.append(vertex)

    if len(path) == len(graph):
        return path
    
    return [] # there is a cycle, return empty list

steps = [ (line[5], line[36]) for line in open("input.txt").readlines() ]
last = set(map(operator.itemgetter(1), steps)) - set(map(operator.itemgetter(0), steps))
graph = defaultdict(list)
graph[last.pop()] = []

for s in steps:
    graph[s[0]] += [s[1]]

result = topological_sort(graph)
print("".join(result))
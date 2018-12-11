import operator
from collections import defaultdict

def topological_sort(graph):
    in_degree = { e : 0 for e in graph }
    for edge in graph:
        for vertex in graph[edge]:
            in_degree[vertex] += 1

    to_visit = list(filter(lambda x: in_degree[x] == 0, in_degree))
    path = []
    while to_visit:
        edge = min(to_visit)
        to_visit.remove(edge)
        path.append(edge)
        for vertex in graph[edge]:
            in_degree[vertex] -= 1
            if in_degree[vertex] == 0:
                to_visit.append(vertex)

    if len(path) == len(graph):
        return path
    
    return [] # there is a cycle, return empty list

steps = [ (line[5], line[36]) for line in open("input.txt").readlines() ]
last = set(map(operator.itemgetter(1), steps)) - set(map(operator.itemgetter(0), steps))
graph = defaultdict(list)
graph[last.pop()] = []

for s in steps:
    graph[s[0]] += [s[1]]

ordered_steps = topological_sort(graph)

workers = { i: ('', 0) for i in range(5) }
time = 0
actual_steps = ''
total_length = len(ordered_steps)
while total_length > len(actual_steps):
    for i, worker in workers.items():
        if worker[1] <= time:
            actual_steps += worker[0]
            if worker[0] in graph:
                del graph[worker[0]]
            workers[i] = ('', 0)

            deps = set([i for s in graph.values() for i in s])
            for s in ordered_steps:
                if s not in deps:
                    ordered_steps.remove(s)
                    workers[i] = (s, time + 60 + ord(s) - 64)
                    break

    # print(time, workers)
    time += 1

print(time - 1)

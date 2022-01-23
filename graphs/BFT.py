# Breadth first traversal
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def bft(graph, start):
    queue = [start]
    while len(queue) > 0:
        current = queue[0]
        queue.pop(0)
        print(current)
        for neightbor in graph[current]:
            queue.append(neightbor)


bft(graph, 'a')

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

graph = {}


def edgesToGraph(edges):
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)


def shorter_path(edges, start, end):
    edgesToGraph(edges)
    return explore(graph, start, end)


visited_nodes = []


def explore(graph, start, end):
    queue = [[start, 0]]
    while len(queue) > 0:
        current, count = queue[0]
        queue.pop(0)
        if current == end:
            return count
        visited_nodes.append(current)
        for adj in graph[current]:
            if adj not in visited_nodes:
                queue.append([adj, count+1])

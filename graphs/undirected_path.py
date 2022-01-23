edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def undirected_path(edges, node_A, node_B):
    edgeToGraph(edges)
    return bfs(graph, node_A, node_B)


graph = {}
visited = []


def edgeToGraph(edges):
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)


def bfs(graph, start, end):
    queue = [start]
    while len(queue) > 0:
        current = queue[0]
        queue.pop(0)
        visited.append(current)
        if current == end:
            return True
        for adj in graph[current]:
            if adj not in visited:
                queue.append(adj)
    return False

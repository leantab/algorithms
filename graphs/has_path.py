graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path(graph, start, end):
    queue = [start]
    while len(queue) > 0:
        current = queue[0]
        queue.pop(0)
        if current == end:
            return True
        for adj in graph[current]:
            queue.append(adj)

    return False


def has_path_rdfs(graph, start, end):
    if start == end:
        return True
    for adj in graph[start]:
        if has_path_rdfs(graph, adj, end):
            return True
    return False


print(has_path(graph, 'f', 'k'))
print(has_path_rdfs(graph, 'f', 'k'))

print(has_path(graph, 'f', 'j'))
print(has_path_rdfs(graph, 'f', 'j'))

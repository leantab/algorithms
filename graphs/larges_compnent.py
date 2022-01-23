graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}
visited = []


def largest_component(graph):
    max_val = 0
    for node in graph:
        if node not in visited:
            new_val = explore(graph, node)
            if new_val > max_val:
                max_val = new_val
    return max_val


def explore(graph, node):
    if node in visited:
        return 0

    count = 1

    visited.append(node)

    for adj in graph[node]:
        count += explore(graph, adj)

    return count

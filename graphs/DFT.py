# Depth first traversal
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def dft(graph, start):
    stack = [start]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for adj in graph[current]:
            stack.append(adj)


def recursive_dft(graph, start):
    print(start)
    for adj in graph[start]:
        recursive_dft(graph, adj)


dft(graph, 'a')
print('---------------------')
recursive_dft(graph, 'a')

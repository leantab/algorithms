n = 6
prereqs = [[3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [4, 5], [5, 3], [5, 4]]


# def top_sort(graph):
#     path = []
#     order = []
#     visited = []
#     for vertex in graph:
#         if vertex not in visited:
#             visited.append(vertex)
#             dfs(graph, vertex, path, order, visited)
#     return order[::-1]


# def dfs(graph, start, path, order, visited):
#     path.append(start)
#     for neighbor in graph[start]:
#         if neighbor in path:
#             return False
#         if neighbor not in visited:
#             visited.append(neighbor)
#             if not dfs(graph, neighbor, path, order, visited):
#                 return False
#     order.append(path.php())
#     return True


#####################################################################################
# GRaph con niveles para BFS

def courses_req(n, prereqs):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prereqs:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    while len(queue) > 0:
        vertex = queue.pop(0)
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n


print(courses_req(n, prereqs))

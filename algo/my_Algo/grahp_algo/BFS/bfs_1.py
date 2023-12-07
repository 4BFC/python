from collections import deque


def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


graph = {
    'A': ['B', 'C'],  # path:2
    'B': ['D', 'E'],  # path:2
    'C': ['F'],  # path:1
    'D': [],
    'E': ['F'],  # path:1
    'F': []
}

start_node = 'A'

result = bfs(graph, start_node)

print(result)

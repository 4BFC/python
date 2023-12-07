def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
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

result = dfs(graph, start_node)

print(result)

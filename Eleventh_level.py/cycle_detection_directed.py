def has_cycle(graph, num_vertices):
    visited = [False] * num_vertices
    in_recursion_stack = [False] * num_vertices

    def dfs(node):
        visited[node] = True
        in_recursion_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif in_recursion_stack[neighbor]:
                return True  # back edge -> cycle

        in_recursion_stack[node] = False  # unmark on way out
        return False

    for vertex in range(num_vertices):
        if not visited[vertex]:
            if dfs(vertex):
                return True
    return False

num_vertices = 3
graph = [
    [1],    # 0 -> 1
    [2],    # 1 -> 2
    [0]     # 2 -> 0
]

print(has_cycle(graph, num_vertices))  # True
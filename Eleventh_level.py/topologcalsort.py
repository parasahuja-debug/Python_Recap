def topological_sort(num_vertices, adjacency_list):
    visited = [False] * num_vertices
    finish_stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        finish_stack.append(node)  # push on finish

    for node in range(num_vertices):
        if not visited[node]:
            dfs(node)

    return finish_stack[::-1]

num_vertices = 6
adjacency_list = [
    [],      # 0 → nothing
    [],      # 1 → nothing
    [3],     # 2 → 3
    [1],     # 3 → 1
    [0, 1],  # 4 → 0, 4 → 1
    [0, 2],  # 5 → 0, 5 → 2
]

print(topological_sort(num_vertices, adjacency_list))
# e.g. [5, 4, 2, 3, 1, 0]  (one valid order — not unique)
#Edges: 5 → 0, 4 → 0, 5 → 2, 2 → 3, 3 → 1, 4 → 1
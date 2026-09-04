# def has_cycle_dfs(num_vertices, adjacency_list):
#     visited = [False] * num_vertices

#     def dfs(current_node, parent_node):
#         visited[current_node] = True
#         for neighbor in adjacency_list[current_node]:
#             if not visited[neighbor]:
#                 if dfs(neighbor, current_node):
#                     return True
#             elif neighbor != parent_node:
#                 # visited neighbor that isn't parent -> cycle
#                 return True
#         return False  

#     for start_node in range(num_vertices):
#         if not visited[start_node]:
#             if dfs(start_node, -1):
#                 return True
#     return False

from collections import deque

def has_cycle_bfs(num_vertices, adjacency_list):
    visited = [False] * num_vertices

    def bfs(start_node):
        visited[start_node] = True
        queue = deque([(start_node, -1)])  # (node, parent)

        while queue:
            current_node, parent_node = queue.popleft()
            for neighbor in adjacency_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current_node))
                elif neighbor != parent_node:
                    return True
        return False

    for start_node in range(num_vertices):
        if not visited[start_node]:
            if bfs(start_node):
                return True
    return False


num_vertices = 3
adjacency_list = [
    [1, 2],   # node 0 connects to 1, 2
    [0, 2],   # node 1 connects to 0, 2
    [0, 1]    # node 2 connects to 0, 1
]

print(has_cycle_dfs(num_vertices, adjacency_list))  # True
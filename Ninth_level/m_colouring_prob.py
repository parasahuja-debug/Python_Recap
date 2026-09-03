# Statement: Given an undirected graph (as adjacency matrix) and m colors, 
# determine if the graph can be colored such that no two adjacent vertices 
# share the same color. Return true/false (or find one valid coloring).

# This is backtracking, same skeleton as N-Queens: 
# place a color, check if it's safe, recurse, backtrack if it fails.

# Approach
# colors[] array tracks the color assigned to each vertex (0 if unassigned).
# At each vertex v, try colors 1 to m.
# A color c is safe for v if no adjacent vertex already has color c.
# Recurse to vertex v+1. If all vertices get colored, success.
# Backtrack (reset colors[v] = 0) if no color works.
def graph_coloring(graph, num_colors):
    num_vertices = len(graph)
    colors = [0] * num_vertices

    def is_safe(vertex, color):
        for neighbor in range(num_vertices):
            # graph[vertex][neighbor] == 1 means they are adjacent
            if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
                return False
        return True

    def solve(vertex):
        if vertex == num_vertices:
            return True  # all vertices colored

        for color in range(1, num_colors + 1):
            if is_safe(vertex, color):
                colors[vertex] = color
                if solve(vertex + 1):
                    return True
                colors[vertex] = 0  # backtrack

        return False  # no color worked for this vertex

    if solve(0):
        return colors
    return None

# graph = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [0, 1, 1, 0]
# ]
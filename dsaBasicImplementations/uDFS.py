graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# using recursion
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# using iteration
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:

        node = stack.pop()
        if node in visited:
            continue       # already handled via another path

        visited.add(node)
        order.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order

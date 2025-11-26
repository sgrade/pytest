def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # Process node
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Process node
            stack.extend(n for n in graph[node] if n not in visited)


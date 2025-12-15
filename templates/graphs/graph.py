from collections import defaultdict


def build_graph(edges, directed=False):
    """
    Build an adjacency list graph from a list of edges.

    Args:
        edges: List of (u, v) tuples representing edges
        directed: If True, create directed graph; otherwise undirected

    Returns:
        dict: Adjacency list representation {node: [neighbors]}
    """
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph


def build_weighted_graph(edges, directed=False):
    """
    Build a weighted adjacency list graph from edges.

    Args:
        edges: List of (u, v, weight) tuples
        directed: If True, create directed graph; otherwise undirected

    Returns:
        dict: Adjacency list {node: [(neighbor, weight), ...]}
    """
    graph = defaultdict(list)

    for u, v, weight in edges:
        graph[u].append((v, weight))
        if not directed:
            graph[v].append((u, weight))

    return graph


# Example usage
if __name__ == "__main__":
    from bfs import bfs
    from dfs import dfs, dfs_iterative

    # Undirected graph
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    graph = build_graph(edges)

    print("Graph:", dict(graph))
    print("BFS from 0:", bfs(graph, 0))
    print("DFS from 0:", dfs(graph, 0))
    print("DFS iterative from 0:", dfs_iterative(graph, 0))

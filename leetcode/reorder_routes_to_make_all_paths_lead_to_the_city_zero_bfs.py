# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/


# Based on Editorial's Approach 2: Breadth First Search
from collections import deque


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Bidirectional graph: 1 if the original road points this way.
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for src, dst in connections:
            adj[src].append((dst, 1))
            adj[dst].append((src, 0))

        def bfs(start: int) -> int:
            # Count roads pointing away from 0 on the unique path to 0.
            reorders = 0
            visited = [False] * n
            q = deque([start])
            visited[start] = True

            while q:
                node = q.popleft()
                for neighbor, direction in adj[node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    reorders += direction
                    q.append(neighbor)

            return reorders

        return bfs(0)

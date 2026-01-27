# 3650. Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

import heapq
from math import inf


# Based on Editorial's Approach: Dijkstra
class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w * 2))

        costs = [inf] * n
        visited = [False] * n
        costs[0] = 0
        heap = [(0, 0)]

        while heap:
            cur_cost, u = heapq.heappop(heap)
            if u == n - 1:
                return cur_cost
            if visited[u]:
                continue
            visited[u] = True

            for v, w in adj[u]:
                next_cost = cur_cost + w
                if next_cost < costs[v]:
                    costs[v] = next_cost
                    heapq.heappush(heap, (next_cost, v))

        return -1

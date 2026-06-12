# 3559. Number of Ways to Assign Edge Weights II
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/


# Based on Editorial's Approach: Lowest Common Ancestor (LCA) + Mathematics
import math

MOD = 10**9 + 7


class Solution:
    def assignEdgeWeights(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        n = len(edges) + 1
        log = max(1, math.ceil(math.log2(n)))
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * (n + 1)
        # up[k][x] is the 2^k-th ancestor of x (0 means no ancestor).
        up = [[0] * (n + 1) for _ in range(log + 1)]

        # Iterative DFS from root (node 1) to set depths and direct parents.
        stack = [(1, 0)]
        while stack:
            x, parent = stack.pop()
            up[0][x] = parent
            for y in adj[x]:
                if y != parent:
                    depth[y] = depth[x] + 1
                    stack.append((y, x))

        # Binary lifting: the 2^k ancestor is the 2^(k-1) ancestor twice over.
        for k in range(1, log + 1):
            for x in range(1, n + 1):
                up[k][x] = up[k - 1][up[k - 1][x]]

        def lca(x: int, y: int) -> int:
            if depth[x] < depth[y]:
                x, y = y, x
            # Lift the deeper node up to the same depth.
            diff = depth[x] - depth[y]
            for k in range(log + 1):
                if diff >> k & 1:
                    x = up[k][x]
            if x == y:
                return x
            # Lift both together until their parents coincide.
            for k in range(log, -1, -1):
                if up[k][x] != up[k][y]:
                    x, y = up[k][x], up[k][y]
            return up[0][x]

        # For a path of d edges, the sum is odd iff an odd number of edges have
        # weight 1, which can be chosen in 2^(d-1) ways. d = du + dv - 2*d_lca.
        res = []
        for x, y in queries:
            d = depth[x] + depth[y] - 2 * depth[lca(x, y)]
            res.append(pow(2, d - 1, MOD) if d else 0)
        return res

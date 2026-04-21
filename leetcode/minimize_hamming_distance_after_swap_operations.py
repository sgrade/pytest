# 1722. Minimize Hamming Distance After Swap Operations
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

# Based on Editorial's Approach: Hash Table + Union-Find

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(
        self,
        source: list[int],
        target: list[int],
        allowedSwaps: list[list[int]],
    ) -> int:
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        # For each component root, count available source values.
        groups: dict = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            groups[uf.find(i)][source[i]] += 1

        # Match each target value against its component's source pool.
        ans = 0
        for i in range(n):
            pool = groups[uf.find(i)]
            if pool[target[i]] > 0:
                pool[target[i]] -= 1
            else:
                ans += 1
        return ans

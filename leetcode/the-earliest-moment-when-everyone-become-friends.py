# 1101. The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]
    def find (self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union_set (self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return 0
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return 1

class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        logs.sort(key = lambda log: log[0])
        dsu = UnionFind(n)
        sets = n
        for timestamp, x, y in logs:
            sets -= dsu.union_set(x, y)
            if sets == 1:
                return timestamp
        return -1

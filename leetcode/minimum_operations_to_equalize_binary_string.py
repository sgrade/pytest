# 3666. Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

import sys
from collections import deque

from sortedcontainers import SortedList


# Based on Editorial's Approach: Breadth-First Search
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n, m = len(s), s.count("0")
        inf = sys.maxsize
        dist = [inf] * (n + 1)
        node_sets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]
        q = deque([m])
        dist[m] = 0
        node_sets[m % 2].remove(m)
        while q:
            m = q.popleft()
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1
            node_set = node_sets[lnode % 2]
            idx = node_set.bisect_left(lnode)
            while idx < len(node_set) and node_set[idx] <= rnode:  # type: ignore[operator]
                m2: int = node_set[idx]  # type: ignore[assignment]
                dist[m2] = dist[m] + 1
                q.append(m2)
                node_set.pop(idx)
        return -1 if dist[0] == inf else dist[0]

# 3161. Block Placement Queries
# https://leetcode.com/problems/block-placement-queries/

from sortedcontainers import SortedList


# Based on Editorial's Approach: Segment Tree.
# Each obstacle position stores the gap to its left neighbour. A query asks
# whether some gap in [0, x] (or the free space just left of x) fits a block.
class Solution:
    # Right sentinel sits one past the largest possible position (5 * 10^4),
    # so every real position has a neighbour to its right.
    MAX_POS = 50001

    def _update(self, idx: int, val: int, node: int, lo: int, hi: int) -> None:
        # Point update: set the gap at position idx, then pull up the max.
        if lo == hi:
            self.seg[node] = val
            return
        mid = (lo + hi) >> 1
        if idx <= mid:
            self._update(idx, val, node << 1, lo, mid)
        else:
            self._update(idx, val, node << 1 | 1, mid + 1, hi)
        self.seg[node] = max(self.seg[node << 1], self.seg[node << 1 | 1])

    def _query(self, ql: int, qr: int, node: int, lo: int, hi: int) -> int:
        # Range query: largest gap among positions in [ql, qr].
        if ql <= lo and hi <= qr:
            return self.seg[node]
        mid = (lo + hi) >> 1
        res = 0
        if ql <= mid:
            res = max(res, self._query(ql, qr, node << 1, lo, mid))
        if qr > mid:
            res = max(res, self._query(ql, qr, node << 1 | 1, mid + 1, hi))
        return res

    def getResults(self, queries: list[list[int]]) -> list[bool]:
        mx = self.MAX_POS
        self.seg = [0] * ((mx + 1) << 2)
        obstacles = SortedList([0, mx])
        self._update(mx, mx, 1, 0, mx)  # initial gap from 0 to mx
        ans = []

        for q in queries:
            if q[0] == 1:
                # Place an obstacle at x, splitting the gap it falls into.
                x = q[1]
                idx = obstacles.bisect_right(x)
                left: int = obstacles[idx - 1]  # type: ignore[assignment]
                right: int = obstacles[idx]  # type: ignore[assignment]
                self._update(x, x - left, 1, 0, mx)
                self._update(right, right - x, 1, 0, mx)
                obstacles.add(x)
            else:
                # Can a block of size sz fit anywhere in [0, x]?
                x, sz = q[1], q[2]
                pre: int = obstacles[obstacles.bisect_right(x) - 1]  # type: ignore[assignment]
                # Best of: free space just left of x, or any earlier gap.
                max_space = max(x - pre, self._query(0, pre, 1, 0, mx))
                ans.append(max_space >= sz)

        return ans

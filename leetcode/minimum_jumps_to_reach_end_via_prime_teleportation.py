# 3629. Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

# Based on Editorial's Approach 2: Forward Breadth-First Search

from collections import defaultdict

# Sieve: for each number, collect all its prime factors.
_MX = 1_000_001
_factors: list[list[int]] = [[] for _ in range(_MX)]
for _p in range(2, _MX):
    if not _factors[_p]:  # _p is prime
        for _k in range(_p, _MX, _p):
            _factors[_k].append(_p)


class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)

        # Map prime -> indices whose value is divisible by that prime.
        edges: dict[int, list[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            for p in _factors[num]:
                edges[p].append(i)

        dist = 0
        seen = [False] * n
        seen[0] = True
        q = [0]

        while True:
            nxt: list[int] = []
            for i in q:
                if i == n - 1:
                    return dist
                # ±1 jumps.
                for neighbor in (i - 1, i + 1):
                    if 0 <= neighbor < n and not seen[neighbor]:
                        seen[neighbor] = True
                        nxt.append(neighbor)
                # Prime teleportation: when nums[i] is prime, jump to every
                # index sharing that prime factor, then clear the group so
                # each prime edge is relaxed at most once.
                if len(_factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            nxt.append(j)
                    edges[p].clear()
            q = nxt
            dist += 1

# 1345. Jump Game IV
# https://leetcode.com/problems/jump-game-iv/

from collections import defaultdict


# Based on Editorial's Approach 2: Bidirectional BFS
class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        # value -> list of indices with that value
        graph = defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)

        from_start = {0}  # BFS frontier from start
        from_end = {n - 1}  # BFS frontier from end
        visited = {0, n - 1}
        ans = 0

        while from_start:
            # always expand the smaller frontier
            if len(from_start) > len(from_end):
                from_start, from_end = from_end, from_start
            nxt = set()

            for node in from_start:
                # jump to any index with the same value
                for child in graph[arr[node]]:
                    if child in from_end:
                        return ans + 1
                    if child not in visited:
                        visited.add(child)
                        nxt.add(child)
                graph[arr[node]].clear()  # prevent redundant revisits

                # jump to adjacent indices
                for child in (node - 1, node + 1):
                    if child in from_end:
                        return ans + 1
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nxt.add(child)

            from_start = nxt
            ans += 1

        return -1

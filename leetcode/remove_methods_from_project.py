# 3310. Remove Methods From Project
# https://leetcode.com/problems/remove-methods-from-project/

from collections import deque


# Based on Editorials Approach: Searching
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        # Directed graph: caller invokes callee.
        graph = [[] for _ in range(n)]
        for caller, callee in invocations:
            graph[caller].append(callee)

        # Every method reachable from k is suspicious.
        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        while queue:
            method = queue.popleft()
            for callee in graph[method]:
                if not suspicious[callee]:
                    suspicious[callee] = True
                    queue.append(callee)

        # Removal is only allowed if no external method invokes a
        # suspicious one; otherwise keep the whole project.
        for caller, callee in invocations:
            if not suspicious[caller] and suspicious[callee]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]

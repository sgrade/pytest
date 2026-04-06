# 582. Kill Process
# https://leetcode.com/problems/kill-process/


from collections import defaultdict


# Based on Editorial's Approach #3 HashMap + Depth First Search
class Solution:
    def killProcess(
        self, pid: list[int], ppid: list[int], kill: int
    ) -> list[int]:
        children: dict[int, list[int]] = defaultdict(list)
        for child, parent in zip(pid, ppid, strict=True):
            children[parent].append(child)

        # DFS to collect the killed process and all its descendants.
        result = []
        stack = [kill]
        while stack:
            node = stack.pop()
            result.append(node)
            stack.extend(children[node])
        return result

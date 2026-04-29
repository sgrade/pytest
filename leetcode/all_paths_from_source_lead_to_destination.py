# 1059. All Paths from Source Lead to Destination
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

# Based on Editorial: DFS; three colors (None = WHITE, GRAY, BLACK).


class Solution:
    GRAY = 1
    BLACK = 2

    def leadsToDestination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        graph = self._build_digraph(n, edges)
        return self._leads_to_dest(graph, source, destination, [None] * n)

    def _leads_to_dest(
        self,
        graph: list[list[int]],
        node: int,
        dest: int,
        states: list[int | None],
    ) -> bool:
        # Already seen: BLACK → subtree OK; GRAY → back-edge (cycle).
        if states[node] is not None:
            return states[node] == Solution.BLACK

        if not graph[node]:
            return node == dest

        states[node] = Solution.GRAY
        for nxt in graph[node]:
            if not self._leads_to_dest(graph, nxt, dest, states):
                return False

        states[node] = Solution.BLACK
        return True

    def _build_digraph(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        return graph

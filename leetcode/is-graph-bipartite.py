# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n
        for i in range(n):
            if visited[i] != -1:
                continue
            visited[i] = 0
            st = []
            st.append(i)
            while st:
                j = st.pop()
                for neigh in graph[j]:
                    if visited[neigh] == -1:
                        st.append(neigh)
                        visited[neigh] = not visited[j]
                    elif visited[j] == visited[neigh]:
                        return False
        return True

# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import deque


# Based on Editorial's Approach 1: Topological Sort (Kahn's Algorithm)
class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> bool:
        # Edge prerequisite -> course; in_degree[c] is remaining prereqs for c.
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            in_degree[course] += 1

        # Start with courses that have no remaining prerequisites.
        queue = deque()
        for course in range(numCourses):
            if not in_degree[course]:
                queue.append(course)

        courses_visited = 0
        while queue:
            course = queue.popleft()
            courses_visited += 1
            # Taking a course unlocks dependents; enqueue when all prereqs
            # are done.
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if not in_degree[next_course]:
                    queue.append(next_course)

        # A cycle leaves leftover in-degree, so not all courses are visited.
        return courses_visited == numCourses

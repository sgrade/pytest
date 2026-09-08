# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


# Based on Editorial's Approach 2: Depth First Search
class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = [False] * numCourses
        in_stack = [False] * numCourses

        def has_cycle(course: int) -> bool:
            if in_stack[course]:
                return True
            if visited[course]:
                return False
            visited[course] = True
            in_stack[course] = True

            # A course already on this path creates a circular dependency.
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True
            in_stack[course] = False
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True

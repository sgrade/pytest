# 1086. High Five
# https://leetcode.com/problems/high-five/

import heapq
from collections import defaultdict


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        # Group every score by student id.
        scores: dict[int, list[int]] = defaultdict(list)
        for student_id, score in items:
            scores[student_id].append(score)

        # Average the five highest scores, ids in increasing order.
        return [
            [student_id, sum(heapq.nlargest(5, student_scores)) // 5]
            for student_id, student_scores in sorted(scores.items())
        ]

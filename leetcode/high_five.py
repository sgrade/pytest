# 1086. High Five
# https://leetcode.com/problems/high-five/


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:

        items.sort()
        ans: list[list[int]] = []

        id = items[0][0]
        scores: list = []
        for item in items:
            cur_id, cur_score = item[0], item[1]
            if cur_id == id:
                scores.append(cur_score)
            else:
                scores.sort(reverse=True)
                top_five_average = sum(scores[: min(len(scores), 5)]) // 5
                ans.append([id, top_five_average])
                id = cur_id
                scores = [cur_score]

        if scores:
            scores.sort(reverse=True)
            top_five_average = sum(scores[: min(len(scores), 5)]) // 5
            ans.append([id, top_five_average])

        return ans

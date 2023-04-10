# 1244. Design A Leaderboard
# https://leetcode.com/problems/design-a-leaderboard/

# Based on Leetcode's Editorial Approach 3
from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.top_scores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.top_scores[score] = self.top_scores.get(score, 0) + 1
            return
        
        # else
        pre_score = self.scores[playerId]
        val = self.top_scores.get(pre_score)
        if val == 1:
            del self.top_scores[pre_score]
        else:
            self.top_scores[pre_score] -= 1
        new_score = pre_score + score
        self.scores[playerId] = new_score
        self.top_scores[new_score] = self.top_scores.get(new_score, 0) + 1

    def top(self, K: int) -> int:
        cnt = 0
        top_k_sum = 0
        for score in self.top_scores.keys()[::-1]:
            times = self.top_scores.get(score)
            for _ in range(times):
                top_k_sum += score
                K -= 1
                if K == 0:
                    break
            if K == 0:
                break
        return top_k_sum

    def reset(self, playerId: int) -> None:
        pre_score = self.scores[playerId]
        if self.top_scores[pre_score] == 1:
            del self.top_scores[pre_score]
        else:
            self.top_scores[pre_score] -= 1
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

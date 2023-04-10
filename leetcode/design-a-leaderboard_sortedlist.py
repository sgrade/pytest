# 1244. Design A Leaderboard
# https://leetcode.com/problems/design-a-leaderboard/

from sortedcontainers import SortedList

class Leaderboard:

    def __init__(self):
        # playerId -> score
        self.scores = {}
        # list of tuples (score, playerId)
        self.top_scores = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if  playerId in self.scores:
            self.top_scores.remove((self.scores[playerId], playerId))
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score
        self.top_scores.add((self.scores[playerId], playerId))

    def top(self, K: int) -> int:
        top_k_sum = 0
        idx = -1
        while K > 0:
            top_k_sum += self.top_scores[idx][0]
            idx -= 1
            K -= 1
        return top_k_sum

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            self.top_scores.remove((self.scores[playerId], playerId))
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

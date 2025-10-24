# 3387. Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

from typing import List
from collections import defaultdict, deque


# Based on https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/solutions/6147735/easy-bfs
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        for i, p in enumerate(pairs1):
            cur1, cur2 = p
            rate = rates1[i]
            adj1[cur1].append((cur2, rate))
            adj1[cur2].append((cur1, 1 / rate))
        for i, p in enumerate(pairs2):
            cur1, cur2 = p
            rate = rates2[i]
            adj2[cur1].append((cur2, rate))
            adj2[cur2].append((cur1, 1 / rate))
        max_amount_day1 = self.bfs(adj1, initialCurrency, 1.0)
        ans = 0.0
        for cur, amt in max_amount_day1.items():
            max_amount_day2 = self.bfs(adj2, cur, amt)
            ans = max(ans, max_amount_day2[initialCurrency])
        return ans

        
    def bfs(self, adj, start_cur, start_amount):
        max_amount = defaultdict(float)
        max_amount[start_cur] = start_amount
        q = deque([(start_cur, start_amount)])
        while q:
            cur, amt = q.popleft()
            for nxt_cur, rate in adj[cur]:
                nxt_amt = amt * rate
                if nxt_amt > max_amount[nxt_cur]:
                    max_amount[nxt_cur] = nxt_amt
                    q.append((nxt_cur, nxt_amt))
        return max_amount


if __name__ == "__main__":
    initialCurrency = "C"
    pairs1 = [["C","OX"]]
    rates1 = [1.5]
    pairs2 = [["C","OX"]]
    rates2 = [9.4]
    print(Solution().maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2))

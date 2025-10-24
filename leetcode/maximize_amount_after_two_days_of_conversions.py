# 3387. Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

from typing import List
from collections import defaultdict, deque


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # Build graphs for both days
        adj1 = self.build_graph(pairs1, rates1)
        adj2 = self.build_graph(pairs2, rates2)
        
        # Day 1: Find max amount for each reachable currency
        day1_amounts = self.bfs(adj1, initialCurrency, 1.0)
        
        # Day 2: Try converting back from each currency
        ans = 1.0  # At minimum, we can keep initial currency
        for currency, amount in day1_amounts.items():
            day2_amounts = self.bfs(adj2, currency, amount)
            if initialCurrency in day2_amounts:
                ans = max(ans, day2_amounts[initialCurrency])
        
        return ans
    
    def build_graph(self, pairs, rates):
        graph = defaultdict(list)
        for (cur1, cur2), rate in zip(pairs, rates):
            graph[cur1].append((cur2, rate))
            graph[cur2].append((cur1, 1 / rate))
        return graph
    
    def bfs(self, graph, start_currency, start_amount):
        max_amount = {start_currency: start_amount}
        queue = deque([(start_currency, start_amount)])
        
        while queue:
            current_currency, current_amount = queue.popleft()
            for next_currency, rate in graph[current_currency]:
                next_amount = current_amount * rate
                if next_amount > max_amount.get(next_currency, 0):
                    max_amount[next_currency] = next_amount 
                    queue.append((next_currency, next_amount))
        
        return max_amount

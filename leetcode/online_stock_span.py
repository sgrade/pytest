# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/

# Based on Editorial's Approach: Monotonic Stack
class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        ans = 1
        while self.st and self.st[-1][0] <= price:
            ans += self.st.pop()[1]
        self.st.append([price, ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

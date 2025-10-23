# 2034. Stock Price Fluctuation 
# https://leetcode.com/problems/stock-price-fluctuation/

import heapq


class StockPrice:

    def __init__(self):
        self.ts_to_price = {}
        self.min_heap = []
        self.max_heap = []
        self.current_price = 1000000000
        self.current_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.ts_to_price[timestamp] = price
        if timestamp >= self.current_timestamp:
            self.current_price = price
            self.current_timestamp = timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.current_price

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]
        while self.ts_to_price[timestamp] != -price:
            heapq.heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]
        while self.ts_to_price[timestamp] != price:
            heapq.heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.storage = [[] for i in range(7)]

    def put(self, key: int, value: int) -> None:
        bucket = key % 7
        for pair in self.storage[bucket]:
            if pair[0] == key:
                pair[1] = value
                return
        self.storage[bucket].append([key, value])

    def get(self, key: int) -> int:
        bucket = key % 7
        for pair in self.storage[bucket]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = key % 7
        for idx, pair in enumerate(self.storage[bucket]):
            if pair[0] == key:
                del self.storage[bucket][idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

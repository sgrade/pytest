# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.storage = [[] for i in range(2069)]        

    def add(self, key: int) -> None:
        bucket = key % 2069
        for element in self.storage[bucket]:
            if element == key:
                return
        self.storage[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 2069
        for idx, element in enumerate(self.storage[bucket]):
            if element == key:
                del self.storage[bucket][idx]

    def contains(self, key: int) -> bool:
        bucket = key % 2069
        for element in self.storage[bucket]:
            if element == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import choice


class RandomizedSet:
    def __init__(self):
        self.val_to_idx: dict[int, int] = {}
        self.idx_to_val: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        idx = len(self.idx_to_val)
        self.val_to_idx[val] = idx
        self.idx_to_val.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        val_idx = self.val_to_idx[val]

        last_val = self.idx_to_val[-1]
        self.val_to_idx[last_val] = val_idx
        self.idx_to_val[val_idx] = last_val

        self.idx_to_val.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return choice(self.idx_to_val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

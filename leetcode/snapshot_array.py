# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/

import bisect


# My own solution optimized with ideas from Leetcode's Sample 532 ms submission
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_ar = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snap_ar[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect(self.snap_ar[index], snap_id, key=lambda p: p[0]) - 1
        return self.snap_ar[index][idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

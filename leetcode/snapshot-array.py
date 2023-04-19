# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/

import bisect

# Memory Limit Exceeded
# Based on Leetcode's Sample 434 ms submission
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_ar = {}
        self.current = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        self.snap_ar[self.snap_id] = dict(self.current)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_ar[snap_id].get(index, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

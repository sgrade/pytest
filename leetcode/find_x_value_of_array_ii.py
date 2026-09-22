# 3525. Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/


# Based on Editorial's Approach: Segment Tree
class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.k = k
        self.length = len(nums)
        tree_size = 2 << self.length.bit_length()

        # Each node stores prefix counts, then its total product remainder.
        self.tree = [[0] * (k + 1) for _ in range(tree_size)]
        self._build(nums, 1, 0, self.length - 1)

    def _set_leaf(self, node: int, value: int) -> None:
        remainder = value % self.k
        node_data = [0] * (self.k + 1)
        node_data[remainder] = 1
        node_data[self.k] = remainder
        self.tree[node] = node_data

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        left_product = left[self.k]
        merged = left.copy()

        # Add prefixes spanning all of the left child and part of the right.
        for remainder, count in enumerate(right[: self.k]):
            merged[(left_product * remainder) % self.k] += count

        merged[self.k] = (left_product * right[self.k]) % self.k
        return merged

    def _refresh(self, node: int) -> None:
        self.tree[node] = self._merge(
            self.tree[node * 2], self.tree[node * 2 + 1]
        )

    def _build(
        self,
        nums: list[int],
        node: int,
        left_bound: int,
        right_bound: int,
    ) -> None:
        if left_bound == right_bound:
            self._set_leaf(node, nums[left_bound])
            return

        midpoint = (left_bound + right_bound) // 2
        self._build(nums, node * 2, left_bound, midpoint)
        self._build(nums, node * 2 + 1, midpoint + 1, right_bound)
        self._refresh(node)

    def _update(
        self,
        node: int,
        left_bound: int,
        right_bound: int,
        index: int,
        value: int,
    ) -> None:
        if left_bound == right_bound:
            self._set_leaf(node, value)
            return

        midpoint = (left_bound + right_bound) // 2
        if index <= midpoint:
            self._update(node * 2, left_bound, midpoint, index, value)
        else:
            self._update(
                node * 2 + 1, midpoint + 1, right_bound, index, value
            )

        self._refresh(node)

    def update(self, index: int, value: int) -> None:
        self._update(1, 0, self.length - 1, index, value)

    def _query(
        self,
        node: int,
        left_bound: int,
        right_bound: int,
        query_left: int,
        query_right: int,
    ) -> list[int]:
        if query_left <= left_bound and right_bound <= query_right:
            return self.tree[node]

        midpoint = (left_bound + right_bound) // 2
        if query_right <= midpoint:
            return self._query(
                node * 2,
                left_bound,
                midpoint,
                query_left,
                query_right,
            )
        if query_left > midpoint:
            return self._query(
                node * 2 + 1,
                midpoint + 1,
                right_bound,
                query_left,
                query_right,
            )

        left = self._query(
            node * 2, left_bound, midpoint, query_left, query_right
        )
        right = self._query(
            node * 2 + 1,
            midpoint + 1,
            right_bound,
            query_left,
            query_right,
        )
        return self._merge(left, right)

    def query_from(self, start: int) -> list[int]:
        return self._query(1, 0, self.length - 1, start, self.length - 1)


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        segment_tree = SegmentTree(nums, k)

        answers = []
        for index, value, start, target_remainder in queries:
            segment_tree.update(index, value)
            prefix_counts = segment_tree.query_from(start)
            answers.append(prefix_counts[target_remainder])

        return answers

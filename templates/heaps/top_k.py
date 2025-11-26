import heapq
from collections import Counter


def find_kth_largest(nums, k):
    """Find Kth largest element using Min Heap."""
    # O(N log K) time, O(K) space
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def top_k_frequent(nums, k):
    """Find Top K frequent elements."""
    # O(N log K) time
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def merge_k_sorted_lists(lists):
    """Merge K sorted lists/arrays."""
    # O(N log K) where N is total elements, K is number of lists
    min_heap = []

    # Add first element from each list to heap
    # (val, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result

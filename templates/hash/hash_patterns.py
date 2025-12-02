from collections import Counter, defaultdict


def two_sum(nums, target):
    """Find indices of two numbers that add to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def group_anagrams(strs):
    """Group strings that are anagrams of each other."""
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def contains_duplicate(nums):
    """Check if array contains duplicates."""
    return len(nums) != len(set(nums))


def first_unique_char(s):
    """Find index of first non-repeating character. -1 if none."""
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


def intersection(nums1, nums2):
    """Find intersection of two arrays (unique elements)."""
    return list(set(nums1) & set(nums2))


def subarray_sum_equals_k(nums, k):
    """Count subarrays with sum equal to k."""
    count = 0
    prefix_sum = 0
    seen = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count


def longest_consecutive(nums):
    """Length of longest consecutive sequence."""
    num_set = set(nums)
    max_len = 0
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            max_len = max(max_len, length)
    return max_len

# 3886. Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-sortable-integers/


from math import isqrt


# Based on Editorial's Approach 1: KMP
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        def get_divisors(num: int) -> set[int]:
            divisors = set()
            for d in range(1, isqrt(num) + 1):
                if num % d == 0:
                    divisors.update((d, num // d))
            return divisors

        def contains(text: list[int], pattern: list[int]) -> bool:
            # KMP: build the prefix function of the pattern.
            prefix = [0] * len(pattern)
            matched = 0
            for i in range(1, len(pattern)):
                while matched and pattern[i] != pattern[matched]:
                    matched = prefix[matched - 1]
                if pattern[i] == pattern[matched]:
                    matched += 1
                prefix[i] = matched

            # Scan the text, reusing the prefix function on mismatches.
            matched = 0
            for value in text:
                while matched and value != pattern[matched]:
                    matched = prefix[matched - 1]
                if value == pattern[matched]:
                    matched += 1
                if matched == len(pattern):
                    return True
            return False

        def is_rotation(block: list[int], target: list[int]) -> bool:
            # Every rotation of a block is a substring of the doubled block.
            return contains(block * 2, target)

        ans = 0
        for size in get_divisors(n):
            # Each block must be rotatable into its slice of the sorted array.
            if all(
                is_rotation(
                    nums[start : start + size],
                    sorted_nums[start : start + size],
                )
                for start in range(0, n, size)
            ):
                ans += size

        return ans

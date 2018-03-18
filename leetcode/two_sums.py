# https://leetcode.com/problems/two-sum/description/

"""Given an array of integers, return indices of the two numbers such that they add up to a
specific target. You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None:
            return [-1, -1]
        else:
            hash_list = []
            index = -1
            for number in nums:
                supplement = target - number
                index += 1
                if supplement in hash_list:
                    # return [hash_list.index(supplement), nums.index(number)]
                    return [hash_list.index(supplement), index]
                else:
                    hash_list.append(number)
            else:
                return [-1, -1]


x = Solution()
print(x.twoSum([2, 7, 11, 15], 9))
print(x.twoSum([3, 3], 6))
# https://leetcode.com/problems/two-sum/description/

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
            for number in nums:
                supplement = target - number
                if supplement in hash_list:
                    return [hash_list.index(supplement), nums.index(number)]
                else:
                    hash_list.append(number)
            else:
                return [-1, -1]

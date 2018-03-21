# https://leetcode.com/problems/maximum-subarray/description/
# solution:
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm_(Algorithm_3:_Dynamic_Programming)


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = nums[0]
        for number in nums[1:]:
            max_ending_here = max(number, max_ending_here + number)
            print('max_ending_here', max_ending_here)
            max_so_far = max(max_ending_here, max_so_far)
            print('max_so_far', max_so_far)
        return max_so_far


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
x = Solution()
print(x.maxSubArray(a))
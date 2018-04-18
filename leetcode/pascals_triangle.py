# https://leetcode.com/problems/pascals-triangle/description/

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        triangle = list()

        if numRows == 0:
            return triangle

        # if numRows == 0, triangle will have just one row
        triangle.append([1])

        # helper function calculating next row of the trianble
        def calc_next_row(prev_row):
            next_row = [1]
            j = 1
            while j < (len(prev_row)):
                next_row.append(prev_row[j-1] + prev_row[j])
                j += 1
            next_row.append(1)
            triangle.append(next_row)

        # index variable to count number of rows in the triangle
        i = 1
        # control block calling the helper function
        while i != numRows:
            previous_row = triangle[-1]
            calc_next_row(previous_row)
            i += 1

        # returning the result
        return triangle


sol = Solution()
inp = 5
print(sol.generate(inp))

def prefix_sum_1d(nums):
    """
    1D Prefix Sum Template

    Use when: Need to quickly compute sum of any subarray
    Time: O(n) to build, O(1) per query
    Space: O(n)

    prefix[i] = sum of nums[0:i]
    Sum of nums[i:j] = prefix[j] - prefix[i]
    """
    n = len(nums)
    prefix = [0] * (n + 1)  # Extra space to avoid index out of bounds

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    return prefix


def range_sum_query(prefix, left, right):
    """
    Query sum of range [left, right] inclusive using prefix sum

    Args:
        prefix: prefix sum array (built with extra space at index 0)
        left: start index (0-based)
        right: end index (0-based, inclusive)

    Returns:
        Sum of elements from left to right
    """
    return prefix[right + 1] - prefix[left]


def prefix_sum_2d(matrix):
    """
    2D Prefix Sum Template

    Use when: Need to quickly compute sum of any submatrix
    Time: O(m*n) to build, O(1) per query
    Space: O(m*n)

    prefix[i][j] = sum of all elements in rectangle from (0,0) to (i-1,j-1)
    """
    if not matrix or not matrix[0]:
        return [[]]

    m, n = len(matrix), len(matrix[0])
    # Extra row and column to avoid index out of bounds
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (
                matrix[i - 1][j - 1]
                + prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
            )

    return prefix


def range_sum_query_2d(prefix, row1, col1, row2, col2):
    """
    Query sum of submatrix from (row1, col1) to (row2, col2) inclusive

    Args:
        prefix: 2D prefix sum array (built with extra row/col at index 0)
        row1, col1: top-left corner (0-based)
        row2, col2: bottom-right corner (0-based, inclusive)

    Returns:
        Sum of elements in the submatrix
    """
    return (
        prefix[row2 + 1][col2 + 1]
        - prefix[row1][col2 + 1]
        - prefix[row2 + 1][col1]
        + prefix[row1][col1]
    )


class PrefixSum1D:
    """
    Object-oriented approach for 1D prefix sum with range queries
    """

    def __init__(self, nums):
        """Build prefix sum array"""
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def range_sum(self, left, right):
        """Query sum of range [left, right] inclusive"""
        return self.prefix[right + 1] - self.prefix[left]


class PrefixSum2D:
    """
    Object-oriented approach for 2D prefix sum with submatrix queries
    """

    def __init__(self, matrix):
        """Build 2D prefix sum array"""
        if not matrix or not matrix[0]:
            self.prefix = [[]]
            return

        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.prefix[i - 1][j]
                    + self.prefix[i][j - 1]
                    - self.prefix[i - 1][j - 1]
                )

    def range_sum(self, row1, col1, row2, col2):
        """Query sum of submatrix from (row1, col1) to (row2, col2) inclusive"""
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


def prefix_sum_with_mod(nums, mod):
    """
    Prefix sum with modulo operation

    Useful when dealing with large numbers that need to be modded
    """
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = (prefix[i] + nums[i]) % mod

    return prefix


def prefix_count(nums, target):
    """
    Count occurrences of each prefix sum value

    Useful for problems like "count subarrays with sum equal to k"
    Pattern: If prefix[j] - prefix[i] = k, then prefix[i] = prefix[j] - k
    """
    from collections import defaultdict

    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # Empty prefix

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        # Check if (current_sum - target) exists
        count += prefix_counts[current_sum - target]
        prefix_counts[current_sum] += 1

    return count


# Example usage
if __name__ == "__main__":
    # Example 1: 1D prefix sum
    nums = [1, 2, 3, 4, 5]
    prefix = prefix_sum_1d(nums)
    print(f"Prefix sum array: {prefix}")  # [0, 1, 3, 6, 10, 15]
    print(f"Sum of nums[1:4]: {range_sum_query(prefix, 1, 3)}")  # 9 (2+3+4)

    # Example 2: Using 1D class
    ps = PrefixSum1D([1, 2, 3, 4, 5])
    print(f"Sum of range [1, 3]: {ps.range_sum(1, 3)}")  # 9

    # Example 3: 2D prefix sum
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    prefix_2d = prefix_sum_2d(matrix)
    print(
        f"Sum of submatrix (1,1) to (2,2): {range_sum_query_2d(prefix_2d, 1, 1, 2, 2)}"
    )  # 28

    # Example 4: Using 2D class
    ps2d = PrefixSum2D(matrix)
    print(f"Sum of submatrix (0,0) to (1,1): {ps2d.range_sum(0, 0, 1, 1)}")  # 12

    # Example 5: Count subarrays with sum equal to target
    nums = [1, 1, 1, 2, 2]
    target = 3
    count = prefix_count(nums, target)
    print(f"Number of subarrays with sum {target}: {count}")  # 4

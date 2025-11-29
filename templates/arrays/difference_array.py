def difference_array_range_update(length, updates):
    """
    Difference Array (Range Addition) Template

    Use when: Need to perform multiple range updates efficiently
    Time: O(n + m) where n is array length, m is number of updates
    Space: O(n)

    Example problem: Apply multiple range increments to an array
    updates = [[start1, end1, inc1], [start2, end2, inc2], ...]
    """
    # Initialize difference array
    diff = [0] * length

    # Apply all updates to difference array
    for start, end, inc in updates:
        diff[start] += inc
        if end + 1 < length:
            diff[end + 1] -= inc

    # Convert difference array back to original array using prefix sum
    ans = [0] * length
    ans[0] = diff[0]
    for i in range(1, length):
        ans[i] = ans[i - 1] + diff[i]

    return ans


def difference_array_from_array(arr):
    """
    Build difference array from an existing array

    diff[i] = arr[i] - arr[i-1] (for i > 0)
    diff[0] = arr[0]

    Use when: Need to convert array to difference array for range updates
    """
    n = len(arr)
    if n == 0:
        return []

    diff = [0] * n
    diff[0] = arr[0]

    for i in range(1, n):
        diff[i] = arr[i] - arr[i - 1]

    return diff


def reconstruct_from_difference(diff):
    """
    Reconstruct original array from difference array using prefix sum

    arr[i] = sum(diff[0] to diff[i])
    """
    n = len(diff)
    if n == 0:
        return []

    arr = [0] * n
    arr[0] = diff[0]

    for i in range(1, n):
        arr[i] = arr[i - 1] + diff[i]

    return arr


class DifferenceArray:
    """
    Object-oriented approach for difference array with range updates

    Useful for multiple range updates with queries
    """

    def __init__(self, size):
        """Initialize with array of given size (all zeros)"""
        self.diff = [0] * size
        self.size = size

    def range_add(self, start, end, value):
        """
        Add value to range [start, end] (inclusive)
        Time: O(1)
        """
        if start < 0 or end >= self.size or start > end:
            return

        self.diff[start] += value
        if end + 1 < self.size:
            self.diff[end + 1] -= value

    def get_array(self):
        """
        Get the final array after all updates
        Time: O(n)
        """
        ans = [0] * self.size
        ans[0] = self.diff[0]

        for i in range(1, self.size):
            ans[i] = ans[i - 1] + self.diff[i]

        return ans


# Example usage
if __name__ == "__main__":
    # Example 1: Range updates
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    ans = difference_array_range_update(length, updates)
    print(f"After range updates: {ans}")  # [-2, 0, 3, 5, 3]

    # Example 2: Using class
    diff_arr = DifferenceArray(5)
    diff_arr.range_add(1, 3, 2)
    diff_arr.range_add(2, 4, 3)
    diff_arr.range_add(0, 2, -2)
    print(f"Using class: {diff_arr.get_array()}")  # [-2, 0, 3, 5, 3]

    # Example 3: Convert array to difference array and back
    original = [3, 5, 2, 8, 6]
    diff = difference_array_from_array(original)
    print(f"Difference array: {diff}")  # [3, 2, -3, 6, -2]
    reconstructed = reconstruct_from_difference(diff)
    print(f"Reconstructed: {reconstructed}")  # [3, 5, 2, 8, 6]

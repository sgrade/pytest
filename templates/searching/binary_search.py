def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_left(arr, target):
    """Find leftmost insertion point (bisect_left). Returns first index >= target."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def binary_search_right(arr, target):
    """Find rightmost insertion point (bisect_right). Returns first index > target."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# ============================================================================
# Using Python's bisect module (preferred in most cases)
# ============================================================================

from bisect import bisect_left, bisect_right


def find_exact(arr, target):
    """Find index of target in sorted array, or -1 if not found."""
    i = bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return i
    return -1


def find_first_ge(arr, target):
    """Find first index >= target (insertion point for target)."""
    return bisect_left(arr, target)


def find_first_gt(arr, target):
    """Find first index > target."""
    return bisect_right(arr, target)


def find_last_le(arr, target):
    """Find last index <= target, or -1 if all elements > target."""
    i = bisect_right(arr, target)
    return i - 1  # -1 if no element <= target


def find_last_lt(arr, target):
    """Find last index < target, or -1 if all elements >= target."""
    i = bisect_left(arr, target)
    return i - 1  # -1 if no element < target


def count_in_range(arr, lo, hi):
    """Count elements in range [lo, hi] inclusive."""
    return bisect_right(arr, hi) - bisect_left(arr, lo)


def count_less_than(arr, target):
    """Count elements < target."""
    return bisect_left(arr, target)


def count_less_equal(arr, target):
    """Count elements <= target."""
    return bisect_right(arr, target)


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]

    # Basic searches
    print(f"Array: {arr}")
    print(f"find_exact(arr, 2): {find_exact(arr, 2)}")  # 1 (first occurrence)
    print(f"find_exact(arr, 6): {find_exact(arr, 6)}")  # -1

    # Boundary searches
    print(f"find_first_ge(arr, 2): {find_first_ge(arr, 2)}")  # 1
    print(f"find_first_gt(arr, 2): {find_first_gt(arr, 2)}")  # 4
    print(f"find_last_le(arr, 2): {find_last_le(arr, 2)}")  # 3
    print(f"find_last_lt(arr, 2): {find_last_lt(arr, 2)}")  # 0

    # Counting
    print(f"count_in_range(arr, 2, 4): {count_in_range(arr, 2, 4)}")  # 5
    print(f"count_less_than(arr, 3): {count_less_than(arr, 3)}")  # 4
    print(f"count_less_equal(arr, 3): {count_less_equal(arr, 3)}")  # 5

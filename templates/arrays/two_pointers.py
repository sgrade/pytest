def two_pointers_opposite(arr, target):
    """Two pointers moving toward each other. Example: Two Sum II (sorted array)."""
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


def two_pointers_same_direction(arr):
    """Fast/slow pointers. Example: Remove duplicates in-place."""
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


def floyd_cycle_detection(head):
    """Detect cycle in linked list. Returns node where cycle begins or None."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle found, find start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

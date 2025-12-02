def next_greater_element(nums):
    """For each element, find next greater element to the right. -1 if none."""
    n = len(nums)
    ans = [-1] * n
    stack = []  # Stores indices
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans


def next_smaller_element(nums):
    """For each element, find next smaller element to the right. -1 if none."""
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            ans[stack.pop()] = nums[i]
        stack.append(i)
    return ans


def prev_greater_element(nums):
    """For each element, find previous greater element to the left. -1 if none."""
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            ans[i] = nums[stack[-1]]
        stack.append(i)
    return ans


def valid_parentheses(s):
    """Check if string has valid matching brackets."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


def daily_temperatures(temps):
    """Days until warmer temperature. 0 if none."""
    n = len(temps)
    ans = [0] * n
    stack = []
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans


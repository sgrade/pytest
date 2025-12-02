def fibonacci(n):
    """Classic 1D DP. O(n) time, O(1) space."""
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def climbing_stairs(n):
    """Ways to climb n stairs (1 or 2 steps). Same as fibonacci."""
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


def house_robber(nums):
    """Max sum of non-adjacent elements."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev, curr = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev, curr = curr, max(curr, prev + nums[i])
    return curr


def coin_change(coins, amount):
    """Min coins to make amount. Returns -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def unique_paths(m, n):
    """Grid paths from top-left to bottom-right (only right/down)."""
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


def longest_common_subsequence(text1, text2):
    """LCS length between two strings."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def knapsack_01(weights, values, capacity):
    """0/1 Knapsack: max value with weight limit."""
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


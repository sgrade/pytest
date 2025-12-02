def subsets(nums):
    """Generate all subsets (power set)."""
    ans = []

    def backtrack(start, path):
        ans.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return ans


def permutations(nums):
    """Generate all permutations."""
    ans = []

    def backtrack(path, used):
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(num)
                backtrack(path, used)
                used[i] = False
                path.pop()

    backtrack([], [False] * len(nums))
    return ans


def combination_sum(candidates, target):
    """Generate combinations that sum to target (candidates can be reused)."""
    ans = []

    def backtrack(remaining, start, path):
        if remaining == 0:
            ans.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(remaining - candidates[i], i, path)  # i because we can reuse
            path.pop()

    backtrack(target, 0, [])
    return ans

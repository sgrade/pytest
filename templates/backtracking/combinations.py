def subsets(nums):
    """Generate all subsets (power set)."""
    res = []

    def backtrack(start, path):
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res


def permutations(nums):
    """Generate all permutations."""
    res = []

    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(num)
                backtrack(path, used)
                used[i] = False
                path.pop()

    backtrack([], [False] * len(nums))
    return res


def combination_sum(candidates, target):
    """Generate combinations that sum to target (candidates can be reused)."""
    res = []

    def backtrack(remaining, start, path):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(remaining - candidates[i], i, path)  # i because we can reuse
            path.pop()

    backtrack(target, 0, [])
    return res

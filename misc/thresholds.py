thresholds = [10, 50, 100] # Sorted
usage = [5, 10, 50, 150]

# Return the list of next thresholds for the given usage. If the usage is greater than the current threshold, the next threshold is -1.
# Complexity should be: O((n + m) * log(n))

def get_next_thresholds(usage, thresholds):
    import bisect
    result = []
    for u in usage:
        pos = bisect.bisect_right(thresholds, u)
        if pos >= len(thresholds):
            result.append(-1)
        else:
            result.append(thresholds[pos])
    return result

def get_next_thresholds_binary(usage, thresholds):
    result = []
    for u in usage:
        left, right = 0, len(thresholds) - 1
        pos = len(thresholds)
        while left <= right:
            mid = (left + right) // 2
            if thresholds[mid] > u:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1
        if pos >= len(thresholds):
            result.append(-1)
        else:
            result.append(thresholds[pos])
    return result

if __name__ == "__main__":
    print(get_next_thresholds(usage, thresholds))
    print(get_next_thresholds_binary(usage, thresholds))

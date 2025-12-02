def merge_intervals(intervals):
    """Merge overlapping intervals."""
    if not intervals:
        return []
    intervals.sort()
    ans = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start, end])
    return ans


def insert_interval(intervals, new):
    """Insert interval and merge if necessary."""
    ans = []
    i = 0
    n = len(intervals)
    # Add all intervals before new
    while i < n and intervals[i][1] < new[0]:
        ans.append(intervals[i])
        i += 1
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    ans.append(new)
    # Add remaining
    while i < n:
        ans.append(intervals[i])
        i += 1
    return ans


def can_attend_meetings(intervals):
    """Check if person can attend all meetings (no overlap)."""
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed."""
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = max_rooms = 0
    s = e = 0
    while s < len(intervals):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    return max_rooms

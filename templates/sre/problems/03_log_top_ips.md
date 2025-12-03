# Problem 3: Find Top K IPs from Logs

**Source:** Common SRE Interview Question (Google, Meta, Amazon)

## Problem Statement

Given a log file in Common Log Format, find the top K IP addresses by request count.

**Log format:** `IP - - [timestamp] "REQUEST" status size`

Example: `192.168.1.1 - - [10/Oct/2023:13:55:36] "GET /api" 200 1234`

## Function Signature

```python
def top_k_ips(log_lines: list[str], k: int) -> list[tuple[str, int]]:
    """
    Find top k IPs by request count.
    
    Returns: list of (ip, count) tuples, sorted by count descending
    """
    pass
```

## Follow-up Questions (commonly asked)

1. What if the log file is too large to fit in memory?
2. How would you handle this in a distributed system?
3. How would you find IPs with error rate > 50%?

## Your Solution

Create your solution in `solutions/03_log_top_ips.py`


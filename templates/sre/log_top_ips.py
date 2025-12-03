"""Problem 3: Find top K IPs from logs."""

import re
from collections import Counter


def top_k_ips(log_lines: list[str], k: int) -> list[tuple[str, int]]:
    """Find top k IPs by request count."""
    ips: list[str] = []
    for line in log_lines:
        match = re.match(r"(\S+)", line)
        if match:
            ips.append(match.group(1))
    return Counter(ips).most_common(k)

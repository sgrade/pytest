import re
from collections import Counter
from typing import TypedDict


class LogEntry(TypedDict):
    ip: str
    timestamp: str
    request: str
    status: int
    size: int


def parse_log_line(line: str) -> LogEntry | None:
    """Parse common log format: IP - - [timestamp] "request" status size"""
    pattern = r'(\S+) .* \[(.*?)\] "(.*?)" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return {
            "ip": match.group(1),
            "timestamp": match.group(2),
            "request": match.group(3),
            "status": int(match.group(4)),
            "size": int(match.group(5)),
        }
    return None


def count_by_field(logs: list[LogEntry | None], field: str) -> Counter[str | int]:
    """Count occurrences by field (e.g., 'ip', 'status')."""
    return Counter(log[field] for log in logs if log)  # type: ignore[literal-required]


def filter_by_status(logs: list[LogEntry | None], status_code: int) -> list[LogEntry]:
    """Filter logs by status code."""
    return [log for log in logs if log and log["status"] == status_code]


def top_k_ips(logs: list[LogEntry | None], k: int) -> list[tuple[str, int]]:
    """Get top k IPs by request count."""
    counts = count_by_field(logs, "ip")
    return counts.most_common(k)  # type: ignore[return-value]


def error_rate(logs: list[LogEntry | None]) -> float:
    """Calculate error rate (5xx responses)."""
    total = len(logs)
    if total == 0:
        return 0
    errors = sum(1 for log in logs if log and log["status"] >= 500)
    return errors / total

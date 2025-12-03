"""Tests for Problem 3: log top IPs."""

from log_top_ips import top_k_ips


def test_top_1(logs_small):
    result = top_k_ips(logs_small, 1)
    assert result == [("1.1.1.1", 3)]


def test_top_2(logs_small):
    result = top_k_ips(logs_small, 2)
    assert result[0] == ("1.1.1.1", 3)
    assert len(result) == 2


def test_empty_logs():
    assert top_k_ips([], 5) == []


def test_tie(logs_tie):
    result = top_k_ips(logs_tie, 1)
    assert result[0][1] == 2  # count is 2

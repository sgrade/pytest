"""Tests for log_parsing template."""

import pytest
from log_parsing import (
    count_by_field,
    error_rate,
    filter_by_status,
    parse_log_line,
    top_k_ips,
)


@pytest.fixture
def sample_logs():
    logs = [
        '1.1.1.1 - - [01/Jan:10:00] "GET /" 200 100',
        '1.1.1.1 - - [01/Jan:10:01] "GET /a" 500 50',
        '2.2.2.2 - - [01/Jan:10:02] "POST /b" 404 25',
    ]
    return [parse_log_line(l) for l in logs]


def test_parse_log_line():
    line = '1.1.1.1 - - [01/Jan:10:00] "GET /" 200 100'
    result = parse_log_line(line)
    assert result["ip"] == "1.1.1.1"
    assert result["status"] == 200


def test_parse_bad_line():
    assert parse_log_line("bad line") is None


def test_count_by_field(sample_logs):
    assert count_by_field(sample_logs, "ip")["1.1.1.1"] == 2
    assert count_by_field(sample_logs, "status")[200] == 1


def test_filter_by_status(sample_logs):
    assert len(filter_by_status(sample_logs, 200)) == 1
    assert len(filter_by_status(sample_logs, 999)) == 0


def test_top_k_ips(sample_logs):
    assert top_k_ips(sample_logs, 1) == [("1.1.1.1", 2)]


def test_error_rate(sample_logs):
    assert error_rate(sample_logs) == pytest.approx(1 / 3)
    assert error_rate([]) == 0

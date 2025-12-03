"""Tests for Problem 1: tail command."""

from tail import tail


def test_last_3_lines(tail_file):
    result = tail(tail_file, 3)
    assert len(result) == 3
    assert "line 8" in result[0]
    assert "line 10" in result[2]


def test_more_than_file_has(tail_file):
    result = tail(tail_file, 100)
    assert len(result) == 10


def test_empty_file(tail_empty_file):
    result = tail(tail_empty_file, 5)
    assert result == []


def test_n_zero(tail_file):
    result = tail(tail_file, 0)
    assert result == []

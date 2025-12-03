"""Shared test fixtures for SRE problems."""

import pytest


# === Problem 1: Tail ===
@pytest.fixture
def tail_file(tmp_path):
    """Create a temp file with 10 lines."""
    f = tmp_path / "test.txt"
    f.write_text("\n".join(f"line {i}" for i in range(1, 11)))
    return str(f)


@pytest.fixture
def tail_empty_file(tmp_path):
    """Create an empty temp file."""
    f = tmp_path / "empty.txt"
    f.write_text("")
    return str(f)


# === Problem 2: Folder Size ===
@pytest.fixture
def fs_small():
    return {
        "root": {"type": "folder", "name": "/", "children": ["f1", "d1"]},
        "f1": {"type": "file", "name": "a.txt", "size": 100},
        "d1": {"type": "folder", "name": "docs", "children": ["f2", "f3"]},
        "f2": {"type": "file", "name": "b.txt", "size": 200},
        "f3": {"type": "file", "name": "c.txt", "size": 50},
    }


@pytest.fixture
def fs_nested():
    return {
        "root": {"type": "folder", "name": "/", "children": ["d1"]},
        "d1": {"type": "folder", "name": "a", "children": ["d2", "f1"]},
        "d2": {"type": "folder", "name": "b", "children": ["f2"]},
        "f1": {"type": "file", "name": "x.log", "size": 10},
        "f2": {"type": "file", "name": "y.log", "size": 5},
    }


@pytest.fixture
def fs_empty():
    return {"root": {"type": "folder", "name": "/", "children": []}}


# === Problem 3: Log Top IPs ===
@pytest.fixture
def logs_small():
    return [
        '1.1.1.1 - - [10/Oct:10:00] "GET /" 200 100',
        '1.1.1.1 - - [10/Oct:10:01] "GET /a" 200 50',
        '2.2.2.2 - - [10/Oct:10:02] "POST /b" 500 25',
        '1.1.1.1 - - [10/Oct:10:03] "GET /c" 404 30',
        '3.3.3.3 - - [10/Oct:10:04] "GET /" 200 100',
    ]


@pytest.fixture
def logs_tie():
    return [
        '10.0.0.1 - - [01/Jan:00:00] "GET /" 200 10',
        '10.0.0.2 - - [01/Jan:00:01] "GET /" 200 10',
        '10.0.0.1 - - [01/Jan:00:02] "GET /" 200 10',
        '10.0.0.2 - - [01/Jan:00:03] "GET /" 200 10',
    ]

"""Tests for Problem 2: folder size."""

from folder_size import folder_size


def test_small_root(fs_small):
    assert folder_size(fs_small, "root") == 350


def test_small_subfolder(fs_small):
    assert folder_size(fs_small, "d1") == 250


def test_single_file(fs_small):
    assert folder_size(fs_small, "f1") == 100


def test_nested(fs_nested):
    assert folder_size(fs_nested, "root") == 15


def test_empty_folder(fs_empty):
    assert folder_size(fs_empty, "root") == 0

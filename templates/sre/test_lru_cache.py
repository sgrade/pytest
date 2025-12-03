"""Tests for lru_cache template."""

from lru_cache import LRUCache


def test_basic_get_put():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("c") == -1


def test_eviction():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")  # access "a" to make "b" LRU
    cache.put("c", 3)  # evicts "b"
    assert cache.get("b") == -1
    assert cache.get("c") == 3


def test_update_existing():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("a", 10)
    assert cache.get("a") == 10

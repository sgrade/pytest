"""Tests for ip_utils template."""

from ip_utils import get_network_info, int_to_ip, ip_in_cidr, ip_to_int, is_valid_ip


def test_is_valid_ip():
    assert is_valid_ip("192.168.1.1") is True
    assert is_valid_ip("::1") is True
    assert is_valid_ip("999.1.1.1") is False
    assert is_valid_ip("abc") is False


def test_ip_in_cidr():
    assert ip_in_cidr("192.168.1.50", "192.168.1.0/24") is True
    assert ip_in_cidr("10.0.0.1", "192.168.1.0/24") is False


def test_get_network_info():
    info = get_network_info("192.168.1.0/24")
    assert info["network"] == "192.168.1.0"
    assert info["broadcast"] == "192.168.1.255"
    assert info["num_hosts"] == 254


def test_ip_to_int():
    assert ip_to_int("0.0.0.1") == 1
    assert int_to_ip(1) == "0.0.0.1"
    assert int_to_ip(ip_to_int("10.0.0.5")) == "10.0.0.5"

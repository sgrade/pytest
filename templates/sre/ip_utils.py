import ipaddress
from typing import TypedDict


class NetworkInfo(TypedDict):
    network: str
    broadcast: str
    netmask: str
    num_hosts: int


def is_valid_ip(ip_str: str) -> bool:
    """Check if string is valid IPv4/IPv6."""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


def ip_in_cidr(ip_str: str, cidr: str) -> bool:
    """Check if IP is in CIDR range."""
    return ipaddress.ip_address(ip_str) in ipaddress.ip_network(cidr, strict=False)


def get_network_info(cidr: str) -> NetworkInfo:
    """Get network info from CIDR."""
    net = ipaddress.ip_network(cidr, strict=False)
    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "netmask": str(net.netmask),
        "num_hosts": net.num_addresses - 2,
    }


def ip_to_int(ip_str: str) -> int:
    """Convert IP to integer (useful for range checks)."""
    return int(ipaddress.ip_address(ip_str))


def int_to_ip(num: int) -> str:
    """Convert integer to IP string."""
    return str(ipaddress.ip_address(num))

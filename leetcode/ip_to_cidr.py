# 751. IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/


# Based on https://leetcode.com/problems/ip-to-cidr/solutions/3330832/short-python-solution-by-yin22-gcjg
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def to_int(address: str) -> int:
            # Treat the address as a 4-digit base-256 number, like building
            # 3407 via value = value * 10 + digit.
            value = 0
            for octet in address.split("."):
                # << 8 is * 256: frees the low 8 bits; | drops the octet in.
                value = (value << 8) | int(octet)
            return value

        def to_address(value: int) -> str:
            # Inverse: shift each byte down to the bottom and mask it off.
            octets = ((value >> shift) & 255 for shift in (24, 16, 8, 0))
            return ".".join(str(octet) for octet in octets)

        start = to_int(ip)
        remaining = n
        cidrs = []
        while remaining:
            # Double the block while it stays aligned on start and fits.
            host_bits = 0
            block_size = 1
            while (start & block_size) == 0 and block_size << 1 <= remaining:
                block_size <<= 1
                host_bits += 1
            cidrs.append(f"{to_address(start)}/{32 - host_bits}")
            start += block_size
            remaining -= block_size
        return cidrs

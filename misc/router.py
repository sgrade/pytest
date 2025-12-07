# Router

# from dataclasses import dataclass

# @dataclass
# class Packet:
# src str
# dst str

"""
dest -> routing_table -> dest_interface_list -> counter -> used to lb traffic
"""


class Router:
    def __init__(self):
        self.interfaces: list[str] = ["int1", "int2"]
        self.routing_table: dict[str, list[str]] = {
            "dst1": ["int1"],
            "dst2": ["int2"],
        }
        self.interface_in_lb: int = 8
        self.dest_counters: dict[str, int] = {"dst1": 0, "dst2": 0}

    def forward(self, packet: dict) -> str:
        """Forward based on destination."""
        dst = packet.get("dest", None)
        if not dst:
            raise ValueError(f"There is no such destination: {dst}")

        dest_interface_list: list[str] | None = self.routing_table.get(dst, None)
        if not dest_interface_list:
            # TODO: implement unknown dest lookup
            raise Exception("There is no such destination")

        dest_counter: int = self.dest_counters.get(dst, 0)
        dest_interface: str = dest_interface_list[dest_counter]

        # Check if the interface is healthy
        # Make decision based on the health

        self.dest_counters[dst] = (self.dest_counters[dst] + 1) % self.interface_in_lb

        return dest_interface


if __name__ == "__main__":
    packet1 = {"src": "src1", "dest": "dst1"}
    packet2 = {"src": "src2", "dest": "dst1"}
    packet3 = {"src": "src1", "dest": "dst2"}

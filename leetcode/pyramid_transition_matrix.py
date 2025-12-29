# 756. Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/


from collections import defaultdict
from functools import lru_cache


# Based on Editorial's Approach #2: Depth-First Search
class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Build transition map: (left, right) -> set of allowed top blocks
        transitions = defaultdict(set)
        for left, right, top in allowed:
            transitions[left, right].add(top)

        @lru_cache(maxsize=None)
        def can_build_pyramid(layer: str) -> bool:
            """Check if we can build a pyramid starting from the given layer."""
            if len(layer) == 1:
                return True

            # Early termination: check if all pairs have valid transitions
            for i in range(len(layer) - 1):
                if not transitions[layer[i], layer[i + 1]]:
                    return False

            # Use list-based backtracking for efficiency
            def build_next_layer(prefix: list[str], i: int) -> bool:
                """Build next layer using efficient list-based backtracking."""
                if i + 1 == len(layer):
                    next_layer_str = "".join(prefix)
                    return can_build_pyramid(next_layer_str)

                # Try each valid top block for current pair
                for top_block in transitions[layer[i], layer[i + 1]]:
                    prefix.append(top_block)
                    if build_next_layer(prefix, i + 1):
                        return True
                    prefix.pop()  # Backtrack

                return False

            return build_next_layer([], 0)

        return can_build_pyramid(bottom)

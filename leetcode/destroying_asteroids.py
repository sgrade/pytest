# 2126. Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Greedy: destroy from smallest to largest, growing mass each time.
        for asteroid in sorted(asteroids):
            if mass < asteroid:
                return False
            mass += asteroid
        return True

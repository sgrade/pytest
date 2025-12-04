# 2211. Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/


class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        prev = directions[0]
        r_count = prev == "R"
        for i in range(1, len(directions)):
            car = directions[i]
            if car == "L":
                if prev == "R":
                    ans += 1 + r_count
                    prev = "S"
                elif prev == "S":
                    ans += 1
                    prev = "S"
                r_count = 0
            elif car == "S":
                ans += r_count  # All accumulated R's collide with S
                prev = "S"
                r_count = 0
            else:
                prev = "R"
                r_count += 1
        return ans

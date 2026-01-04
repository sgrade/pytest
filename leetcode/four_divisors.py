# 1390. Four Divisors
# https://leetcode.com/problems/four-divisors/

# Based on https://leetcode.com/problems/four-divisors/solutions/7463933/b-ks-solutionjust-math-shortest-code-of-07gxj
class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def get_sum_of_factors(n: int):
            cur_sum, factors = 0, 0
            divisor1 = 2
            while divisor1 * divisor1 <= n:
                if n % divisor1 == 0:
                    divisor2 = n // divisor1
                    if divisor2 == divisor1 or factors > 0:
                        return 0
                    cur_sum += divisor1 + divisor2
                    factors += 2
                divisor1 += 1
            if factors == 0:
                return 0
            return 1 + cur_sum + n

        total_sum = 0
        for n in nums:
            total_sum += get_sum_of_factors(n)
        return total_sum

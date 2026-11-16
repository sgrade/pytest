# 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            lst = [int(c) for c in s]
            new_lst = []
            for start in range(0, len(lst), k):
                end = min(len(lst), start + k)
                sm = sum(lst[start:end])
                new_lst.append(sm)
            lst = new_lst
            s = "".join([str(x) for x in lst])
        return s

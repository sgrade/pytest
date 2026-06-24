# 3700. Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

MOD = 1_000_000_007


# Based on Editorial's Approach: Dynamic Programming + Matrix Exponentiation
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7

        m = r - l + 1
        if n == 1:
            return m

        # dp[v]: zigzag arrays ending at the v-th value with the last step
        # going down. The "up" case is the mirror image, so a single m-sized
        # state suffices (see ZigZag Arrays I). A down-step into v can follow
        # any larger up-step value, which after mirroring becomes a prefix
        # sum: dp_new[v] = sum(dp[0 .. m - 2 - v]).
        trans = [
            [1 if w <= m - 2 - v else 0 for w in range(m)] for v in range(m)
        ]

        def mul(a, b):
            p, q, s = len(a), len(b[0]), len(b)
            res = [[0] * q for _ in range(p)]
            for i in range(p):
                ai, ri = a[i], res[i]
                for k in range(s):
                    if ai[k]:
                        aik, bk = ai[k], b[k]
                        for j in range(q):
                            ri[j] = (ri[j] + aik * bk[j]) % mod
            return res

        # Fast exponentiation of the transition matrix: trans^(n - 1).
        result = [[int(i == j) for j in range(m)] for i in range(m)]
        e = n - 1
        while e:
            if e & 1:
                result = mul(result, trans)
            trans = mul(trans, trans)
            e >>= 1

        # Apply trans^(n-1) to the all-ones initial vector (row sums), then
        # double to count both ending directions.
        dp = sum(sum(row) for row in result) % mod
        return 2 * dp % mod

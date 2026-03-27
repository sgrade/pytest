# 2946. Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/


# Editorial: Approach - Traversal
class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        # Both left and right shifts reduce to the same condition:
        # a[j] == a[(j+k) % n] for all j — so even/odd rows need no distinction.
        rows, cols = len(mat), len(mat[0])
        k %= cols  # shift of n is a full cycle; only the remainder matters

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != mat[i][(j + k) % cols]:
                    return False
        return True

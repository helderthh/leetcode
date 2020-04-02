# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def _uniquePaths(i: int, j: int) -> int:
            if (i,j) in memo:
                return memo[(i,j)]
            
            if j >= m - 1 or i >= n - 1:
                return 1
            
            c = _uniquePaths(i+1, j) + _uniquePaths(i, j+1)
            memo[(i,j)] = c
            return c

        return _uniquePaths(0, 0)


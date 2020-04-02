# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def _numSquares(num):
            if num == 1:
                return 1
            if num in memo:
                return memo[num]
            
            min_count = float("inf")
            for i in range(1, num//2 + 1):
                s = i*i
                if s > num:
                    break
                    
                diff = num - s
                if diff == 0:
                    return 1
                
                c = _numSquares(diff)
                memo[diff] = c
                if c < min_count:
                    min_count = c
            
            memo[num] = 1 + min_count
            return 1 + min_count
        
        return _numSquares(n)

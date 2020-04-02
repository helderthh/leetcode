# 78. Subsets
# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        memo = {}
        n = len(nums)
        
        def _subset(pos):
            if pos in memo:
                return []
            
            if pos >= n:
                return []
            
            res = [[nums[pos]]]
            
            for i in range(pos, n):
                for ss in _subset(i+1):
                    res.append(ss)
                    res.append(nums[pos:i+1] + ss)
            
            memo[pos] = True
            return res
        
        return [[]] + _subset(0)
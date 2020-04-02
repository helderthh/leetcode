# 46. Permutations
# https://leetcode.com/problems/permutations/


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permutations_of(nums)
    
    def permutations_of(self, l):
        if len(l) < 2:
            return [l[:]]

        permutations = []
        
        for i, m in enumerate(l):
            for p in self.permutations_of(l[:i] + l[i+1:]):
                permutations.append([m] + p)
    
        return permutations

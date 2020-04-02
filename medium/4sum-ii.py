# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/


from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        ab_counter = dict()
        for a in A:
            for b in B:
                ab_counter[a+b] = ab_counter.get(a+b, 0) + 1
        for c in C:
            for d in D:
                res += ab_counter.get(-(c+d), 0)

        return res

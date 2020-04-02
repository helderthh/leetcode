# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        for i in nums:
            heapq.heappush(l, -i)
            
        for _ in range(k-1):
            heapq.heappop(l)
        
        return -heapq.heappop(l)
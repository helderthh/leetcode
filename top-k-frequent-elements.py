# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/



import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        counts = {}
        
        # count
        for item in nums:
            counts[item] = counts.get(item, 0) + 1
        
        h = []
        for item, count in counts.items():
            heapq.heappush(h, (-count, item))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])

        return res



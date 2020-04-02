# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = bisect.bisect_left(nums, target)
        if left == n or nums[left] != target:
            return [-1, -1]
        
        right = left
        while right < n and nums[left] == nums[right]:
            right += 1
        
        
        return [left, right-1]



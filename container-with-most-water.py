# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/


import bisect

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            max_area = max(max_area, h * abs(left-right))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_area




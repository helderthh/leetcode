# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = -1
        last_one = -1
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0 and last_zero < n - 1:
                nums[last_zero+1], nums[i] = nums[i], nums[last_zero+1]
                last_zero += 1
                last_one += 1
                if nums[i] == 1 and i > 1 and nums[i-1] == 2 and last_one < n:
                    nums[last_one], nums[i] = nums[i], nums[last_one]
            elif nums[i] == 1 and last_one < n - 1:
                nums[last_one+1], nums[i] = nums[i], nums[last_one+1]
                last_one += 1
                
            
        
        
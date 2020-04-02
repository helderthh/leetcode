# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return [] + nums
        
        acum = 1
        output = nums[:]
        # go left
        for i in reversed(range(len(nums) - 1)):
            output[i] *= output[i + 1]
        
        # go right
        for i in range(len(output)-1):
            output[i] = acum * output[i+1]
            acum *= nums[i]
        
        output[-1] = acum
        return output
        
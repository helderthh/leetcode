# 384. Shuffle an Array
# https://leetcode.com/problems/shuffle-an-array/


class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]
        self.reset()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.data = self.orig[:]
        return self.data
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.data)
        for i in range(n):
            rdm_idx = random.randint(0, n-1)
            self.data[i], self.data[rdm_idx] = self.data[rdm_idx], self.data[i]
        
        return self.data
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


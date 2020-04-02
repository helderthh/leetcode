# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/


import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.positions = dict()
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # check if exists
        if val in self.positions:
            return False
        
        # add it to data
        self.data.append(val)
        # add it to positions dict
        self.positions[val] = len(self.data) - 1
        
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # check if exists
        pos = self.positions.get(val)
        if pos is None:
            return False
        
        # swap with last item
        n = len(self.data)
        self.data[pos], self.data[n-1] = self.data[n-1], self.data[pos]
        
        # pop
        self.data.pop()
        # remove it from positions
        del self.positions[val]
        # update swaped element
        if pos != n - 1:
            self.positions[self.data[pos]] = pos
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

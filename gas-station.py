# 134. Gas Station
# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        remain, lack, res = 0, 0, 0
        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                res = i+1
                lack += remain
                remain = 0
        return res if remain+lack>=0 else -1
                
            
            


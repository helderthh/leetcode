# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/


import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        memo = set()
        
        m = matrix  # alias
        h = [(m[0][0], 0,0)]  # heap
        
        count = 0
        i, j = 0, 0
        
        while count != k:
            t = heapq.heappop(h)
            i, j = t[1], t[2]
            if (i,j) in memo:
                continue
                
            print(count, m[i][j])
            memo.add((i,j))
            
            # add right
            if j < n-1:
                t = (m[i][j+1], i, j+1)
                heapq.heappush(h, t)
                
            # add bottom
            if i < n-1:
                t = (m[i+1][j], i+1, j)
                heapq.heappush(h, t)
            
            count += 1
        
        return m[i][j]
            
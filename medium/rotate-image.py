# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            self._rotate_layer(matrix, i)
    
    def _rotate_layer(self, m, layer):
        n = len(m)
        for i in range(layer, n-layer-1):
            aux = m[layer][i]
            
            # move from top to right border
            m[i][n-layer-1], aux = aux, m[i][n-layer-1]
            
            # move from right to bottom border
            m[n-layer-1][n-i-1], aux = aux, m[n-layer-1][n-i-1]
            
            # move from bottom to left border
            m[n-i-1][layer], aux = aux, m[n-i-1][layer]
            
            # update top
            m[layer][i] = aux
            
        


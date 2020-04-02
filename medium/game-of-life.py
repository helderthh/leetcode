# 289. Game of Life
# https://leetcode.com/problems/game-of-life/


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                items = [
                    (i-1, j-1), # top-left
                    (i-1, j), # top
                    (i-1, j+1),  # top-right
                    (i, j-1),  # left
                    (i, j+1),  # right
                    (i+1, j-1),  # bottom-left
                    (i+1, j),  # bottom
                    (i+1, j+1),  # bottm-right
                ]
                for x, y in items:
                    if x < 0 or x >= m:
                        continue
                    if y < 0 or y >= n or board[x][y] == 0:
                        continue
                    
                    count += 1
                
                res = self.final_value(board, i, j, count)
                l.append(res)
            
        x = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = l[x]
                x+=1
                
    def final_value(self, board, x, y, count):
        if board[x][y] == 0:
            return 1 if count == 3 else 0
        else:
            if count < 2 or count > 3:
                return 0
            return 1
        
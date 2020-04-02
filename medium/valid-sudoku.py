36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(l):
            points = 10
            s = set()
            for i in l:
                if i == ".":
                    s.add(points)
                    points += 1
                else:
                    s.add(i)
    
            return len(s) == 9
    
        for i in range(9):
            if not is_valid(board[i]):
                return False
            
            if not is_valid([board[j][i] for j in range(9)]):
                return False
        
        for ii in range(0, 9, 3):
            for jj in range(0, 9, 3):
                l = []
                for i in range(3):
                    for j in range(3):
                        l.append(board[ii+i][jj+j])
                
                if not is_valid(l):
                    return False
        
        return True
        
        
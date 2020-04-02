# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


OPEN = "("
CLOSE = ")"

class Solution:
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n: int) -> List[str]:
        self._generate(n)
        return self.res

    def _generate(self, n, opened=0, closed=0, base=""):
        if base == "":
            self._generate(n, opened + 1, closed, base + OPEN)
            return
        
        if opened == n and closed == n:
            self.res.append(base)
            return
            
        if opened < n:
            self._generate(n, opened + 1, closed, base + OPEN)
        if closed < opened:
            self._generate(n, opened, closed + 1, base + CLOSE)
        

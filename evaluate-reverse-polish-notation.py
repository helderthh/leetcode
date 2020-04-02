# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/


OPERANDS = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "-": lambda x, y: y - x,
    "/": lambda x, y: int(y / x),
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        stack = []
        for item in tokens:
            if item in OPERANDS:
                res = OPERANDS[item](stack.pop(), stack.pop())
                stack.append(res)
            else:
                stack.append(int(item))
        
        return stack.pop()

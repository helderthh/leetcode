# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/


MULTIPLICATION = "*"
SUBSTRACTION = "-"
DIVISION = "/"
SUM = "+"
OPERANDS = [MULTIPLICATION, SUM, SUBSTRACTION, DIVISION]
INVALID = OPERANDS + [" "]


class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        
        # get curr left operand
        left, i = self.number_at(s, 0)
        # while next item is an operand
        while i < n and s[i] in INVALID:
            if s[i] == " ":
                i += 1
                continue
                
            operator = s[i]
            # get right operand
            right, j = self.number_at(s, i+1)
            k = -1
            # check if related with an important operand
            while operator not in [MULTIPLICATION, DIVISION] \
                    and j < n and s[j] in [MULTIPLICATION, DIVISION]:
                # calculate new right value
                other_operand, k = self.number_at(s, j+1)
                right = self.operate(right, s[j], other_operand)
                i = k  # other opetator
                j = k
            
            if k < 0:
                i = j
            left = self.operate(left, operator, right)
            
        return left
    
    def operate(self, a, operand, b):
        if operand is SUM:
            return a + b
        if operand is SUBSTRACTION:
            return a - b
        if operand is MULTIPLICATION:
            return a * b
        if operand is DIVISION:
            return int(a/b)

    def number_at(self, s, i):
        while i < len(s) and s[i] == " ":
            i += 1
        j = i + 1
        while j < len(s) and s[j] not in INVALID:
            j += 1
        ret = int(s[i:j])
        while j < len(s) and s[j] == " ":
            j += 1
        return ret, j

    
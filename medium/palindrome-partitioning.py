# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        self.memo = {}
        self.orig = len(s)
        
        return self._partition(s)
    
    def _partition(self, s, i=0):
        if i in self.memo:
            return self.memo[i]
        if s == "":
            return []
        if i >= self.orig:
            return [[]]
        
        res = []
        
        for j in range(i+1, self.orig+1):
            curr_str = s[i:j]
            if self.is_palindrome(curr_str):
                for partition in self._partition(s, j):
                    res.append([curr_str] + partition)
        
        self.memo[i] = res
        return res
        
    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i- 1]:
                return False
        
        return True

    
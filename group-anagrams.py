# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        n = len(strs)
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            
            l = res.get(ss, [])
            l.append(s)
            res[ss] = l
        
        return res.values()

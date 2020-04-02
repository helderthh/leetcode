# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []  # list of final intervals
        
        # for each interval
        for interval in intervals:
            final_interval = interval
            # for each res
            i = 0
            while i < len(res):
                # check if interval.left is lower or equal res.right
                if self.are_overlapping(final_interval, res[i]):
                    # if it is, merge those intervals
                    final_interval = self._merge(final_interval, res[i])
                    
                    # swap and pop interval
                    res[i], res[-1] = res[-1], res
                    res.pop()
                    i -= 1
                i += 1
            res.append(final_interval)
        
        return res
        
    # insert merged interval
    def are_overlapping(self, a, b):
        return (a[0] <= b[1] \
                and a[1] >= b[0]) \
                or (a[0] >= b[1] \
                and a[1] <= b[0])

    def _merge(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]



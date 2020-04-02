# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        
        for src, tgt in prerequisites:
            g[src].append(tgt)
            
        visited = [0] * numCourses
        
        def hasCycle(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False  # already checked
            
            visited[node] = 1
            for arc in g[node]:
                if hasCycle(arc):
                    return True
            visited[node] = 2
            return False
                
            
        for i in range(numCourses):
            if hasCycle(i):
                return False
        
        return True



# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = self.build_graph([x for x in range(numCourses)], prerequisites)
        visited = [0] * numCourses
        res = deque()
        
        def _dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            

            visited[node] = 1 # mark as visited
            # keep searching
            for arc in g[node]:
                if arc == node:
                    continue
                # print(node, arc)
                if _dfs(arc):
                    return True
            
            visited[node] = 2  # mark as clean (no cycle)
            res.append(node)
            return False
        
        
        # main for
        for i in range(numCourses):
            if _dfs(i):
                return []
        
        path = []
        while res:
            path.append(res.popleft())
        
        return path

    @staticmethod
    def build_graph(nodes, prerequisites):
        g = []
        for node in nodes:
            g.append([])
        for src, tgt in prerequisites:
            s = g[src]
            s.append(tgt)
            g[src] = s
        return g
        

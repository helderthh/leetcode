# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val == root.val:
            return root.val
        
        def _dfs(curr, tgt, path):
            if not curr:
                return False
            if curr.val == tgt.val:
                path.append(curr)
                return True
            
            path.append(curr)
            if _dfs(curr.left, tgt, path):
                return True
            
            if _dfs(curr.right, tgt, path):
                return True
            else:
                path.pop()
                
            return False
        p_path = []
        _ = _dfs(root, p, p_path)
        q_path = []
        _ = _dfs(root, q, q_path)
        # print([x.val for x in p_path])
        # print([x.val for x in q_path])
        i = 0
        n = min(len(p_path), len(q_path))
        while i < n and p_path[i] == q_path[i]:
            i += 1
        
        return p_path[i-1]
        

        
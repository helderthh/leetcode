# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maximum = None
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = root.val
        
        def _max_sum(node):
            if not node:
                return 0
            
            # get left max sum
            left = _max_sum(node.left)
            
            # get right max sum
            right = _max_sum(node.right)
            
            me = node.val
                
            m = max(me, left + me, me + right)
            self.maximum = max(self.maximum, m, left + me + right)
            return m
        
        _max_sum(root)
        return self.maximum
        

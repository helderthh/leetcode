# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def _check(node) -> [TreeNode, TreeNode, bool]:
            if not node:
                return None, None, True
            
            # validate curr node
            if node.left and node.left.val >= node.val:
                return None, None, False
            if node.right and node.right.val <= node.val:
                return None, None, False
            
            min_l, maximum, valid = _check(node.left)
            if maximum is not None and maximum >= node.val or not valid:
                return None, None, False
            
            minimum, max_r, valid = _check(node.right)
            if minimum is not None and minimum <= node.val or not valid:
                return None, None, False
            
            return min_l if min_l is not None else node.val, \
                    max_r if max_r is not None else node.val, True
        
        _,_, res = _check(root)
        return res
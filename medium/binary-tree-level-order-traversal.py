# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
    
        def _traversal(curr_stack):
            new_stack = []
            for node in curr_stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)

            if new_stack:
                res.append([x.val for x in new_stack])
                _traversal(new_stack)
        
        _traversal([root])
        return res


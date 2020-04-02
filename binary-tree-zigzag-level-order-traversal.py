# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        return self._traversal(deque([root]))

    def _traversal(self, nodes: deque) -> List[List[int]]:
        if not nodes:
            return []
        
        res = []
        is_right_dir = True
        
        while nodes:
            init_len = len(nodes)
            new_level = []

            for _ in range(init_len):
                if is_right_dir:
                    node = nodes.popleft()
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                else:
                    node = nodes.pop()
                    if node.right:
                        nodes.appendleft(node.right)
                    if node.left:
                        nodes.appendleft(node.left)
                new_level.append(node.val)

            res.append(new_level)
            is_right_dir = not is_right_dir
        
        return res
    

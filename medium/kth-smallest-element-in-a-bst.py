# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        path = []
        count = 0  # TODO
        while k != count:
            # find the left most element, and fill a path (stack)
            while node.left:
                path.append(node)
                node = node.left
    
            count += 1
            while k != count:
                if node.right:
                    node = node.right
                    break
                else:
                    node = path.pop()
                    count += 1
        
        return node.val


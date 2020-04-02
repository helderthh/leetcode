# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.curr = 0
        
        def search(val, left, right):
            for i in range(left, right+1):
                if inorder[i] == val:
                    return i
            return -1

        def build(left, right):
            if left > right:
                return None
            
            node = TreeNode(preorder[self.curr])
            self.curr += 1
            pos = search(node.val, left, right)
            node.left = build(left, pos-1)
            node.right = build(pos+1, right)
            
            return node
    
        return build(0, len(inorder)-1)

    
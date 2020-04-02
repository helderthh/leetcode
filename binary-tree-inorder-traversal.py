# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorder(root)
    
    def inorder(self, root):
        path = []
        if not root:
            return path
        
        stack = []
        node = root
        while True:
            # if has left child push current node to the stack and move
            # to left child
            if node.left:
                stack.append(node)
                node = node.left
                continue

            # if has right child move there
            if node.right:
                path.append(node.val)
                node = node.right
                continue
            else:  # is leaf
                path.append(node.val)
    
            if not stack:
                break
            node = stack.pop()
            
            # pop while there is no right child
            while stack and not node.right:
                path.append(node.val)
                node = stack.pop()

            # add it and check if we can move to the right child
            path.append(node.val)
            if node.right:
                node = node.right
            else:
                break
    
        return path
    
    def _inorder(self, root, path):
        if not root:
            return
        
        self._inorder(root.left, path)
        path.append(root.val)
        self._inorder(root.right, path)


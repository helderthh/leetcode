# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        stack = collections.deque([root])
        
        while stack:
            new_stack = collections.deque()
            while stack:
                node = stack.popleft()
                if stack:
                    node.next = stack[0]
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        
        return root            
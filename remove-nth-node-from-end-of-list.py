# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return None
        
        # go nth nodes forward
        nth_node = head
        for _ in range(n):
            nth_node = nth_node.next
        
        if not nth_node:
            return head.next
        
        curr = head
        while nth_node.next:
            nth_node = nth_node.next
            curr = curr.next
        
        curr.next = curr.next.next
        return head
        
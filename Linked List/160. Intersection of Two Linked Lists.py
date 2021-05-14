# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:        
        if headA is None or headB is None:
            return None
        
        p1, p2 = headA, headB
        
        while p1 or p2:
            if p1 == p2:
                return p1
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return None
      
      
      
      
# Time - O(m+n)
# Space - O(1)

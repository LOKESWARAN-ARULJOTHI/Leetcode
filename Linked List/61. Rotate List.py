# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k==0:
            return head
        
        tempHead = head
        count = 1
        while tempHead.next:
            count+=1
            tempHead = tempHead.next
        k = k % count
        if k==0:
            return head
        
        tempHead.next = head
        
        move = count - k
        
        lastNode = None
        for _ in range(move):
            lastNode = head
            head=head.next
        lastNode.next = None
        return head
      
      
      
# Time - O(N)
# Space - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        a,b=head,head
        for i in range(1,k):
            a=a.next
        nodeK=a
        a=a.next
        while a:
            a=a.next
            b=b.next
        nodeK.val,b.val=b.val,nodeK.val
        return head

      
      
# Time - O(k)
# Space - O(1)

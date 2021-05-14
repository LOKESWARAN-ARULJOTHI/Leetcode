# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        
        def reverse(head,k):
            curr=head
            length=0
            while curr:
                length+=1
                curr=curr.next
            if k<=1 or length<k:
                return head
            prev=None
            curr=head
            for _ in range(k):
                nextNode=curr.next
                curr.next = prev
                prev=curr
                curr=nextNode
            head.next=reverse(curr,k)
            return prev
        
        return reverse(head,k)
        
        
        
        
# Time - O(N)
# Space - O(1)

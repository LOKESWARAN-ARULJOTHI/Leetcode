# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr=None,head
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev,curr=curr,nextNode
        return prev
        prev, curr = None, head



# Time - O(n)
# Space - O(1)

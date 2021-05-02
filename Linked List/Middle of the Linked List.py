# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid=head
        while head and head.next:
            mid=mid.next
            head=head.next.next
        return mid


# Time - O(n)
# Space - O(1)

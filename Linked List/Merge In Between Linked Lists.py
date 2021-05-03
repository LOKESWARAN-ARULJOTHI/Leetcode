# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        for _ in range(a-1):
            head = head.next
        cur = head.next
        for _ in range(b-a):
            cur = cur.next
        head.next = list2
        while head.next:
            head = head.next
        if cur.next:
            head.next = cur.next
        return list1
                

# Time - O(n), n = max(a,list2)
# Space - O(1)

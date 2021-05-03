# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1=None
        node2=None
        temp=list1
        for i in range(b+1):
            if i==a-1:
                node1=temp
            if i==b:
                node2=temp
            temp=temp.next
        node1.next=list2
        while node1.next:
            node1=node1.next
        node1.next=node2.next
        return list1
                

# Time - O(n), n = list1 + list2
# Space - O(1)

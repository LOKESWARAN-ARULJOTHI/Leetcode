# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=[]
        while head:
            num.append(head.val)
            head=head.next
        length=len(num)
        sum=0
        for i in range(length):
            sum+=(num.pop()*(2**i))
        return sum


# Time - O(N)
# Space - O(1)

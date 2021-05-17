"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        curr=head
        while curr:
            nextNode=curr.next
            curr.next=Node(curr.val)
            curr.next.next=nextNode
            curr=curr.next.next
            
        dummy_head = Node(0)
        cur = dummy_head
        p = head
        
        while p:
            cur.next = p.next
            cur.next.random = p.random.next if p.random else None
            cur = cur.next
            p = p.next.next
        
        return dummy_head.next
            
            
            
            
            
# Time - O(N)
# Space - O(1)

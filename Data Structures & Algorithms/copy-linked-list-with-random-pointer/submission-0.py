"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = Node(head.val)
        new_curr = new_head
        curr = head
        old_to_new = {}
        while curr.next:
            new_node = Node(curr.next.val)
            new_curr.next = new_node
            old_to_new[curr] = new_curr
            curr = curr.next
            new_curr = new_curr.next
        
        new_curr.next = None
        old_to_new[curr] = new_curr
        new_curr = new_head
        curr = head
        while new_curr:
            if curr.random:
                new_curr.random = old_to_new[curr.random]
            else:
                new_curr.random = None
            new_curr = new_curr.next
            curr = curr.next
        
        return new_head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        right = head
        for _ in range(n):
            right = right.next
        
            
        left = head
        if not right:
            return head.next
            
        while right.next:
            right = right.next
            left = left.next

        tmp = left.next.next
        left.next = tmp
        return head
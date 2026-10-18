# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        curr = head
        for i in range((length - 1) // 2):
            curr = curr.next
        
        right = curr.next
        curr.next = None

        curr = right
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        left = head
        right = prev 

        while left:
            l_next = left.next
            r_next = None
            if right:
                r_next = right.next

            left.next = right
            if right:
                right.next = l_next
            left = l_next
            right = r_next
            


            
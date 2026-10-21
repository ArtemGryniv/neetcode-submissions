# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        digit = 1
        curr = l1
        while curr:
            total += digit * curr.val
            curr = curr.next
            digit *= 10

        curr = l2
        digit = 1
        while curr:
            total += digit * curr.val
            curr = curr.next
            digit *= 10

        if total == 0:
            return ListNode(0)

        digit = total % 10
        total //= 10
        new_head = ListNode(digit)
        curr = new_head
        while total > 0:
            digit = total % 10
            curr.next = ListNode(digit)
            total //= 10
            curr = curr.next

        return new_head
            
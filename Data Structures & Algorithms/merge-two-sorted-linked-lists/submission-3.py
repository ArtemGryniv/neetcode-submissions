# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2: 
            return list1



        while list2 and list2.val < list1.val:
            tmp = list2.next
            list2.next = list1
            list1 = list2
            list2 = tmp

        l1 = list1
        while list2 and l1:
            if not l1.next:
                l1.next = list2
                break

            if list2.val <= l1.next.val:
                tmp = list2.next
                list2.next = l1.next
                l1.next = list2
                list2 = tmp

            l1 = l1.next

        return list1



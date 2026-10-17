# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque()
        queue_q = deque()

        queue_p.append(p)
        queue_q.append(q)

        while queue_q:
            curr_q = queue_q.popleft()
            curr_p = queue_p.popleft()
            
            if curr_q and curr_p:
                if curr_q.val != curr_p.val:
                    return False
            elif not curr_q and curr_p:
                return False
            elif curr_q and not curr_p:
                return False
            
            if curr_p:
                queue_p.append(curr_p.left)
                queue_p.append(curr_p.right)

            if curr_q:
                queue_q.append(curr_q.left)
                queue_q.append(curr_q.right)

        return True
            

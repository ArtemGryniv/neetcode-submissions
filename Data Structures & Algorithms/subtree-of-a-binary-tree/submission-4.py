# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        matches = []
        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                matches.append(curr)
            
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        
        if not matches:
            return False

        for match in matches:
            q1 = deque()
            q2 = deque()

            q1.append(match)
            q2.append(subRoot)
            valid = True
            while q1:
                curr1 = q1.popleft()
                curr2 = q2.popleft()
                
                if not curr1 and not curr2:
                    continue
                if not curr1 and curr2:
                    valid = False
                    break
                elif curr1 and not curr2:
                    valid = False
                    break
                
                if curr1.val != curr2.val:
                    valid = False
                    break
                
                q1.append(curr1.right)
                q1.append(curr1.left)
                q2.append(curr2.right)
                q2.append(curr2.left)

            if valid:
                return True

        return False

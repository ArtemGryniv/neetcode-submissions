# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q2 = deque()
        arr = []
        level = []
        q.append(root)
        while q:
            while q:
                curr = q.popleft()
                level.append(curr.val)
            
                if curr.left:
                    q2.append(curr.left)
                if curr.right:
                    q2.append(curr.right)

            arr.append(level)
            level = []
            while(q2):
                q.append(q2.popleft())
            
        return arr
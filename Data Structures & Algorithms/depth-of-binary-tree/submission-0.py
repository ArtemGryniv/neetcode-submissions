# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        num_added = 1
        height = 0
        while q:
            total_added = 0
            while num_added > 0:
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                    total_added += 1
                if curr.right:
                    q.append(curr.right)
                    total_added += 1
                
                num_added -= 1
            
            num_added = total_added
            height += 1
        
        return height
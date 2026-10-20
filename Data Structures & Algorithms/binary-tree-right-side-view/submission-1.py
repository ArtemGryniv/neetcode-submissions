# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = deque()
        q.append(root)
        output = []
        while q:
            right_most = 0
            for _ in range(len(q)):
                curr = q.popleft()
                right_most = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            output.append(right_most.val)
        
        return output
            



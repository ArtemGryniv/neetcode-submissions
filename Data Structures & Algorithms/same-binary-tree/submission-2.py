# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            if p and q:
                if p.val != q.val:
                    return False
            elif not p and q:
                return False
            elif p and not q:
                return False
            

            return dfs(q.left, p.left) and dfs(q.right, p.right)
        
        return dfs(p,q)
            


            
            

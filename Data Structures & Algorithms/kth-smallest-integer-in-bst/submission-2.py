# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        remaining = k
        smallest = 0
        def dfs(root):
            nonlocal remaining
            nonlocal smallest

            if not root or remaining == 0:
                return

            dfs(root.left)

            if remaining == 0:
                return

            remaining -= 1
            if remaining == 0:
                smallest = root.val
                return

            dfs(root.right)

        dfs(root)
        return smallest
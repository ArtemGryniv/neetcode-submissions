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

            if not root:
                return

            dfs(root.left)
            remaining -= 1
            if remaining == 0:
                smallest = root.val

            dfs(root.right)

        dfs(root)
        return smallest
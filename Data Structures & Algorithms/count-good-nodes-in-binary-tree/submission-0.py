# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, max_val):
            nonlocal count

            if not root:
                return

            if root.val >= max_val:
                count += 1
                dfs(root.right, root.val)
                dfs(root.left, root.val)
            else:
                dfs(root.right, max_val)
                dfs(root.left, max_val)

        dfs(root, -100)
        return count

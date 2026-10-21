# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True

        def dfs(root, smallest, largest):
            if not root:
                return True

            if root.val <= smallest or root.val >= largest:
                return False

            return dfs(root.left, smallest, root.val) and dfs(root.right, root.val, largest)


        return dfs(root, float('-inf'), float('inf'))
                

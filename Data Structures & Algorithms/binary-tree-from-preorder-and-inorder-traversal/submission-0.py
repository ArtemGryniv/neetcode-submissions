# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i
        
        index = 0
        def build(left, right):
            nonlocal index

            if left > right:
                return None

            root = TreeNode(preorder[index])
            index += 1

            mid = mp[root.val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        
        return build(0, len(preorder) - 1)



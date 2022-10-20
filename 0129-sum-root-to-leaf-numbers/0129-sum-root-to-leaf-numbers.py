# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(rot, value):
            if rot:
                if not rot.left and not rot.right:
                    value = value*10 + rot.val
                    self.res += value
                dfs(rot.left, value*10 + rot.val)
                dfs(rot.right, value*10 + rot.val)
        dfs(root, 0)
        return self.res
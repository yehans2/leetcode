# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root] if root else res
        
        
        while queue:
            level = []
            nxt_queue = []
            for root in queue:
                level.append(root.val)
                if root.left:
                    nxt_queue.append(root.left)
                if root.right:
                    nxt_queue.append(root.right)
            res.append(level)
            queue = nxt_queue
            
        return res
            
                
                
                
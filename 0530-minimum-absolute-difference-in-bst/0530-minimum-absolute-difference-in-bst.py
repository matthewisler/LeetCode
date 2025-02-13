# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            vals.append(node.val)
            right = dfs(node.right)
        
        vals = []
        dfs(root)
        ans = float("inf")
        for i in range(1, len(vals)):
            ans = min(ans, vals[i] - vals[i-1])
        
        return ans
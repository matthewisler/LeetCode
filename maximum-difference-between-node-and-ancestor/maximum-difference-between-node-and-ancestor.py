# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, max_int, min_int):
            if not node:
                return max_int - min_int
            
            max_int = max(max_int, node.val)
            min_int = min(min_int, node.val)
            left = dfs(node.left, max_int, min_int)
            right = dfs(node.right, max_int, min_int)
            return max(left, right)

        return dfs(root, root.val, root.val)
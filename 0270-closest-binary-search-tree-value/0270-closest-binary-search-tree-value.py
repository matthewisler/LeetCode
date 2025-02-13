# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            if abs(node.val - target) < self.min_diff:
                self.result = node.val
                self.min_diff = abs(node.val - target)

            dfs(node.right)

        self.result = None
        self.min_diff = float("inf")
        dfs(root)
        return self.result
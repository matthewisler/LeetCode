# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if node is None:
                return True
            
            if small < node.val < large:
                left = dfs(node.left, small, node.val)
                right = dfs(node.right, node.val, large)

                return left and right

            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))
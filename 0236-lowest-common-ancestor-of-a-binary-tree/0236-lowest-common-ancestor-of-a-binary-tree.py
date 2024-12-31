# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q

            if left + right + mid > 1:
                self.ans = node
            
            return left or right or mid
        
        dfs(root)
        return self.ans
                
            
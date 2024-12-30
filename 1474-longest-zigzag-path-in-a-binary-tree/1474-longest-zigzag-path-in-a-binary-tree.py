# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest_zz = 0

        def dfs(node, go_left, max_zz):
            nonlocal longest_zz
            if node:
                longest_zz = max(max_zz, longest_zz)
                if go_left:
                    dfs(node.left, False, max_zz+1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, max_zz+ 1)
        
        dfs(root, True, 0)
        return longest_zz
            
        
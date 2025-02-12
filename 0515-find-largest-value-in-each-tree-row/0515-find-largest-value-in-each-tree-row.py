# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        ans = []
        

        while queue:
            current_length = len(queue)
            this_level_max = float("-inf")

            for _ in range(current_length):
                node = queue.popleft()
                this_level_max = max(this_level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(this_level_max)
        return ans
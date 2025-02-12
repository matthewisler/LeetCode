# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            queue_length = len(queue)
            sum_of_level = 0
            for _ in range(queue_length):
                node = queue.popleft()
                sum_of_level += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum_of_level
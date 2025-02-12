# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        depth = -1

        while queue:
            queue_length = len(queue)
            #do something per level
            depth += 1
            this_depth = []
            for _ in range(queue_length):
                node = queue.popleft()
                if depth % 2 == 0:
                    this_depth.append(node.val)
                else:
                    this_depth = [node.val] + this_depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(this_depth)
        return ans
              
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = ans = 0
        nodes = []
        dummy = head
        while dummy:
            nodes.append(dummy.val)
            dummy = dummy.next

        for i in range(int(len(nodes)/2)):
            curr = nodes[i] + nodes[len(nodes)-1-i]
            ans = max(ans, curr)
        
        return ans
        

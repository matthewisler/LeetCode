# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        if head.next == None:
            return None
    
        p1 = p2 = head
        count = 0
        while p1 is not None:
            count += 1
            p1 = p1.next

        node_to_remove = math.floor(count/2)
        print(f"node_to_remove: {node_to_remove}")

        for _ in range(node_to_remove-1):
            p2 = p2.next
        
        p2.next = p2.next.next
        return head
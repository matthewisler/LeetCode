# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        quick = head
        slow = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next

            if quick == slow:
                return True
        return False
        
        
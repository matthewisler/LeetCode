# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        values = []
        while current is not None:
            values.append(current.val)
            current = current.next
        
        i = 0
        j = len(values) - 1
        max_size = 0
        while i < j:
            max_size = max(max_size, values[i] + values[j])
            i+=1
            j-=1
        
        return max_size
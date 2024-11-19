class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distance_left = 0
        for num in nums:
            if distance_left < 0:
                return False
            elif num > distance_left:
                distance_left = num
            distance_left -= 1
        return True
            
            
            
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import math
        if len(nums) <3:
            return False
        min1 = math.inf
        min2 = math.inf
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False
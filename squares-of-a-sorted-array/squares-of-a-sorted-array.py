class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        
        while left < right:
            nums[left] = nums[left]**2
            nums[right] = nums[right]**2
            
            left += 1
            right -= 1
        if left == right:
            nums[left] = nums[left]**2
            
        return sorted(nums)
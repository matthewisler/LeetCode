class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i==0:
                left = 0
                right = sum(nums[i+1:])
            elif i==len(nums)-1:
                left = sum(nums[0:i])
                right = 0
            else:
                left = sum(nums[:i])
                right = sum(nums[i+1:])
            
            if left == right:
                return i

        return -1